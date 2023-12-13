from ...image.dto.descriptor import Descriptor
from ...user.models.user import User
from sklearn.cluster import KMeans
import numpy as np


class ImageSelectionService:
    __n_clusters: int

    def __init__(self, n_clusters: int = 3):
        self.__n_clusters = n_clusters

    def get_relevant_images(self, user: User) -> list:
        vectors = []
        images = []

        if len(user.images) <= self.__n_clusters:
            return user.images

        for image in user.images:
            descriptor = Descriptor.from_json(image.descriptor)
            vectors.append(descriptor.vector)
            images.append(image)

        kmeans = KMeans(n_clusters=self.__n_clusters, n_init="auto")
        predictions = kmeans.fit_predict(vectors)
        distances = kmeans.transform(vectors)
        cluster_map = self.__get_cluster_relevant_images_map(images, predictions, distances)

        relevant_images = []
        for item in [*cluster_map.values()]:
            relevant_images.append(item['image'])

        return relevant_images

    def __get_cluster_relevant_images_map(self, images: list, predictions: list, distances: list) -> dict:
        images_map = {}

        for i in range(len(images)):
            image = images[i]
            cluster = predictions[i]
            distance = np.min(distances[i])

            if cluster not in images_map:
                images_map[cluster] = {"image": image, "distance": distance}
            else:
                relevant_image = images_map[cluster]
                if distance < relevant_image['distance']:
                    images_map[cluster] = {"image": image, "distance": distance}

        return images_map
