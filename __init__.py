from .detection_node import DetectionCustomNode
NODE_CLASS_MAPPINGS = { "Detect Gender, Age, Person Count" : DetectionCustomNode}
NODE_DISPLAY_NAME_MAPPINGS = { "my unique name" : "Detection Node" }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']