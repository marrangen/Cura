from UM.Scene.SceneNodeDecorator import SceneNodeDecorator
from UM.Application import Application
from UM.Logger import Logger


class BuildPlateDecorator(SceneNodeDecorator):
    def __init__(self, build_plate_number = -1):
        super().__init__()
        self._build_plate_number = None
        self.setBuildPlateNumber(build_plate_number)

    def setBuildPlateNumber(self, nr):
        # Make sure that groups are set correctly
        # setBuildPlateForSelection in CuraActions makes sure that no single childs are set.
        self._build_plate_number = nr
        if self._node and self._node.callDecoration("isGroup"):
            for child in self._node.getChildren():
                child.callDecoration("setBuildPlateNumber", nr)

    def getBuildPlateNumber(self):
        return self._build_plate_number

    def __deepcopy__(self, memo):
        return BuildPlateDecorator()