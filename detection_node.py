import json
import torch
import numpy as np
from deepface import DeepFace
from PIL import Image

class DetectionCustomNode:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_in": ("IMAGE",),
                "age_toggle": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "emotion_toggle": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "gender_toggle": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "race_toggle": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"})
            }
        }

    RETURN_TYPES = ("TEXT_TYPE","INT")
    RETURN_NAMES = ("single Person", "people count")

    FUNCTION = "detection"

    CATEGORY = "phantaisia"

    def detection(self,image_in, age_toggle, emotion_toggle, gender_toggle, race_toggle):
        i = 255. * image_in[0].cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        img.save("custom_nodes\\comfyui_detection_node\\test.png")
        # dont know why it is breaking when i not save the image but transform the tensor to an np array [BRG]
        # analyze_results = DeepFace.analyze(image_in[0].detach().cpu().numpy()[..., ::-1], detector_backend="retinaface", enforce_detection=False)
        analyze_results = DeepFace.analyze("custom_nodes\\comfyui_detection_node\\test.png", detector_backend="retinaface", enforce_detection=False)
        recognized_persons = len(analyze_results)
        if recognized_persons == 1:
            age, race, gender, emotion = "","","",""
            result_string = ""
            if age_toggle: result_string += "a " + str(analyze_results[0]["age"]) + " years old "
            if race_toggle: result_string += analyze_results[0]["dominant_race"] + " "
            if gender_toggle: result_string += analyze_results[0]["dominant_gender"] + " "
            if emotion_toggle: result_string += analyze_results[0]["dominant_emotion"]
            result = [result_string, 1]
        else:
            result = ["", recognized_persons]
        print(result)

        return result