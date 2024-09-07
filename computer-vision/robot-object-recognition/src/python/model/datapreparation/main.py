import cv2
import numpy as np
import os
import skimage.io as io

from requests.models import Response
from pycocotools.coco import COCO
from typing import Any
from urllib.request import urlopen


INSTANCES_TRAIN_FILE: str = "data/instances_train2017.json"


class CocoAnnotationsGetter:
    @staticmethod
    def load_annotations(path: str) -> COCO:
        """
        This method is used to load the file instances_train2017 downloaded by the CocoDatasetDownloader.
        :param path:
        :return:
        """
        return COCO(path)

    @staticmethod
    def get_images_by_category(
        instances_annotations: COCO, category: str
    ) -> tuple[int, list[dict[str, Any]]]:
        """
        Given the category name, getCatIds() returns the category ID from the file instances_train2017.

        getImgIds() gets the list of image IDs for the given category.

        :param instances_annotations: The file containing metadata about images.
        :param category: The name of category. Given this name, the metadata about images, that belong to that category,
        are fetched.

        :return: category_id: The category ID, which all images belong to.
        :return: images: The list of objects, that contain metadata such as licence, file_name, coco_url, height, width,
        date_captured, flickr_url, id.
        """
        category_id: int = instances_annotations.getCatIds(catNms=[category])[0]

        image_ids: list[int] = instances_annotations.getImgIds(catIds=category_id)

        images: list[dict[str, Any]] = list()

        for img_id in image_ids:
            image: dict[str, Any] = instances_annotations.loadImgs(img_id)[0]

            images.append(image)

        return category_id, images

    @staticmethod
    def download_images(images: list[dict[str, Any]], category_name: str) -> None:
        """
        Given the metadata about images, fetched from the instances_train2017.json file, the url is used to download
        the image and save it in the .jpg format.

        :param images:
        :param category_name:
        """
        count: int = 0

        for image in images:
            response: Response = urlopen(image.get("coco_url"))

            if response.getcode() == 200:
                image_data: bytes = response.read()

                image_id: int = image.get("id")

                with open(
                    f"data/images/{category_name}/train_image_{image_id}.jpg", "wb"
                ) as f:
                    f.write(image_data)

            else:
                print(f"Response code {response.getcode()}")

            # keep track
            count = count + 1

            if count % 100 == 0:
                print(count)

    @staticmethod
    def get_bounding_boxes_by_image_id(
        instances_annotations: COCO, images: list[dict[str, Any]], category_id: int
    ) -> dict[str, list[list[float]]]:
        """
        Given the metadata about images, fetched from the instances_train2017.json file, all objects bounding boxes,that
        belong to the specified category are returned by this method.

        :param instances_annotations: i.e. instances_train2017.json file
        :param images:
        :param category_id:
        :return: bounding_boxes dict containing the image ID and the list of bounding boxes float values
        """

        bounding_boxes: dict[str, list[list[float]]] = dict()

        for image in images:
            annotations_ids: list[int] = instances_annotations.getAnnIds(
                imgIds=image.get("id")
            )

            instances_annotations_bounding_boxes: list[dict[str, Any]] = (
                instances_annotations.loadAnns(annotations_ids)
            )

            bounding_boxes_one_image: list[list[float]] = list()

            for bounding_box in instances_annotations_bounding_boxes:
                if bounding_box["category_id"] == category_id:
                    bounding_boxes_one_image.append(bounding_box["bbox"])

            bounding_boxes[str(image.get("id"))] = bounding_boxes_one_image

        return bounding_boxes

    @staticmethod
    def crop_images_by_bounding_boxes(
        images: list[dict[str, Any]],
        bounding_boxes_all: dict[str, list[list[float]]],
        category_name: str,
    ) -> None:
        """
        Given the bounding boxes, objects on the image are cropped and saved in the .jpg format.

        :param images:
        :param bounding_boxes_all:
        :param category_name:
        :return:
        """

        count: int = 0

        for image in images:
            image_id: str = str(image.get("id"))

            image_numpy_array: np.ndarray = io.imread(
                f"data/images/{category_name}/train_image_{image_id}.jpg"
            )

            no_objects_in_image: int = 0

            bounding_boxes: list[list[float]] = bounding_boxes_all.get(image_id)

            for bounding_box in bounding_boxes:
                start_x: int = int(bounding_box[0])
                end_x: int = start_x + int(bounding_box[2])

                start_y: int = int(bounding_box[1])
                end_y: int = start_y + int(bounding_box[3])

                try:
                    # 3D array
                    cropped_image: np.ndarray = image_numpy_array[
                                                start_y:end_y, start_x:end_x, :
                                                ]

                    cropped_image: np.ndarray = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2BGR)
                except IndexError:
                    # grayscale 2D array
                    cropped_image: np.ndarray = image_numpy_array[
                                                start_y:end_y, start_x:end_x
                                                ]

                cv2.imwrite(
                    f"data/cropped_images/{category_name}/cropped_train_image_{image_id}_{no_objects_in_image}.jpg",
                    cropped_image,
                )

                no_objects_in_image += 1

                # keep track
                count = count + 1

                if count % 100 == 0:
                    print(count)


def pad_images(category_name: str) -> None:
    """
    After cleaning the images (excl. blured images), empty black canvas is created and all images are placed into it.
    This way we avoid losing some information when resizing images to smaler size then original.

    :return:
    """

    print("padding images")

    images_sample_size: int = 200
    canvas_height: int = 416
    min_image_height: int = 210
    min_image_width: int = 210
    canvas_width: int = 416
    center_x: int = 208
    center_y: int = 208

    successfully_postprocessed_images: list[str] = list()
    skipped_images: list[str] = list()

    for image_name in os.listdir(f"data/cleaned_images/{category_name}"):
        canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

        try:
            image = cv2.imread(f"data/cleaned_images/{category_name}/" + image_name)

            image_width: int = image.shape[1]
            image_height: int = image.shape[0]

            # image height and width cannot be more than canvas_height, canvas_width
            if image_width < canvas_width+1 and image_width > min_image_width and image_height < canvas_height+1 and image_height > min_image_height:

                start_x: int = int(center_x - (image_height / 2))
                end_x: int = int(start_x + image_height)

                start_y: int = int(center_y - (image_width / 2))
                end_y: int = int(start_y + image_width)

                canvas[start_x:end_x, start_y:end_y] = image

                cv2.imwrite(
                    f"data/images_with_padding/{category_name}/cropped_train_image_{image_name}",
                    canvas,
                )

                successfully_postprocessed_images.append(image_name)

        except Exception:
            skipped_images.append(image_name)

        if len(successfully_postprocessed_images) == images_sample_size:
            # we have enough pictures
            break

    print(f"successfully_postprocessed_images {len(successfully_postprocessed_images)}")
    print(f"skipped_images {len(skipped_images)}")


def main() -> None:
    category_name: str = "cup"

    coco_annotations_getter = CocoAnnotationsGetter()

    instances_annotations: COCO = coco_annotations_getter.load_annotations(
        INSTANCES_TRAIN_FILE
    )

    category_id, instances_annotations_images = (
        coco_annotations_getter.get_images_by_category(
            instances_annotations, category_name
        )
    )

    coco_annotations_getter.download_images(instances_annotations_images, category_name)

    bounding_boxes: dict[str, list[list[float]]] = (
        coco_annotations_getter.get_bounding_boxes_by_image_id(
            instances_annotations, instances_annotations_images, category_id
        )
    )

    coco_annotations_getter.crop_images_by_bounding_boxes(
        instances_annotations_images, bounding_boxes, category_name
    )

    pad_images(category_name)


if __name__ == "__main__":
    main()
