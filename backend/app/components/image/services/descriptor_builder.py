import open_clip
import torch
from PIL import Image
from open_clip import CoCa
from io import BytesIO
from ..dto.descriptor import Descriptor


class DescriptorBuilder:
    __model: CoCa
    __transform: any

    def __init__(self):
        print('Load CLIP model...')
        device = "cpu"
        self.__model, _, self.__transform = open_clip.create_model_and_transforms(
            model_name="coca_ViT-L-14",
            pretrained="mscoco_finetuned_laion2B-s13B-b90k",
            device=device,
            cache_dir="files/models"
        )
        print('CLIP model ready')

    def build(self, image_bytes) -> Descriptor:
        bytes_io = BytesIO()
        bytes_io.write(image_bytes)
        image = self.__transform(Image.open(bytes_io).convert("RGB")).unsqueeze(0)
        with torch.no_grad():
            generated = self.__model.generate(image)
            image_features = torch.flatten(self.__model.encode_image(image))
            text = open_clip.decode(generated[0]).split(
                "<end_of_text>"
            )[0].replace(
                "<start_of_text>", ""
            ).replace('.', '').strip()

        return Descriptor(text, image_features.tolist())