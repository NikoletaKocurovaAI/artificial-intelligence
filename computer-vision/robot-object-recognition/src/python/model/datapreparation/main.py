import cv2
import numpy as np
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
        Given the category name, getCatIds() returns the category ID.

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
    def download_images(images: list[dict[str, Any]], category_name: str):
        """
        Given the metadata about images, fetched from the instances_train2017.json file, the url is used to download
        the image and save it in the .jpg format.

        :param images:
        :param category_name:
        :return:
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

        :param instances_annotations:
        :param images:
        :param category_id:
        :return:
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

            break

        return bounding_boxes

    @staticmethod
    def crop_images_by_bounding_boxes(
        images: list[dict[str, Any]],
        bounding_boxes: dict[str, list[list[float]]],
        category_name: str,
    ) -> None:
        """
        Given the bounding boxes, objects on the image are cropped and saved in the .jpg format.

        :param images:
        :param bounding_boxes:
        :param category_name:
        :return:
        """
        for image in images:
            image_id: str = str(image.get("id"))

            image_numpy_array: np.ndarray = io.imread(
                f"data/images/{category_name}/train_image_{image_id}.jpg"
            )

            no_objects_in_image: int = 0

            bounding_boxes: list[list[float]] = bounding_boxes.get(image_id)

            for bounding_box in bounding_boxes:
                start_x: int = int(bounding_box[0])
                end_x: int = start_x + int(bounding_box[2])

                start_y: int = int(bounding_box[1])
                end_y: int = start_y + int(bounding_box[3])

                cropped_image: np.ndarray = image_numpy_array[
                    start_y:end_y, start_x:end_x, :
                ]

                image_numpy_array_bgr: np.ndarray = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2BGR)

                cv2.imwrite(
                    f"data/cropped_images/{category_name}/cropped_train_image_{image_id}_{no_objects_in_image}.jpg",
                    image_numpy_array_bgr,
                )

                no_objects_in_image += 1

    @staticmethod
    def resize_images():
        pass


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

    # coco_annotations_getter.download_images(instances_annotations_images, category_name)

    bounding_boxes: dict[str, list[list[float]]] = (
        coco_annotations_getter.get_bounding_boxes_by_image_id(
            instances_annotations, instances_annotations_images, category_id
        )
    )

    coco_annotations_getter.crop_images_by_bounding_boxes(
        instances_annotations_images, bounding_boxes, category_name
    )


if __name__ == "__main__":
    main()
