import os
import requests


class CocoDatasetDownloader:
    """
    https://cocodataset.org/#download
    """

    def __init__(self) -> None:
        self.ANNOTATIONS_ZIP_FILE: str = "data/annotations_trainval2017.zip"
        self.ANNOTATIONS_URL: str = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"

    def download_annotations(self) -> None:
        count: int = 0

        if not os.path.exists(self.ANNOTATIONS_ZIP_FILE):
            print("file does not exist")
            r = requests.get(self.ANNOTATIONS_URL, stream=True)

            with open(self.ANNOTATIONS_ZIP_FILE, 'wb') as f:
                print("Downlading started")

                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

                    # keep track
                    count = count + 1
                    if count % 100 == 0:
                        print(count)


def main() -> None:
    coco_dataset_downloader = CocoDatasetDownloader()

    coco_dataset_downloader.download_annotations()


if __name__=="__main__":
    main()
