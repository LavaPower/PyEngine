from pyengine import Window, Entity, ControlType
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Utils import Colors, Vec2
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, ControlComponent
from pyengine.Prefabs import Tilemap
from pyengine.Widgets import Checkbox, ProgressBar, Button


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value, debug=True)

        self.uisys = self.world.get_system(UISystem)

        self.check = Checkbox(Vec2(500, 500), "TEST")
        self.check.label.color = Colors.BLACK.value
        self.progress = ProgressBar(Vec2(400, 300), Vec2(300, 20), ("tilemap/sprite0.png", "tilemap/sprite1.png"))
        self.button = Button(Vec2(500, 100), "Add", self.add_progressbar)

        self.uisys.add_widget(self.check)
        self.uisys.add_widget(self.progress)
        self.uisys.add_widget(self.button)

        self.esys = self.world.get_system(EntitySystem)

        self.tilemap = Tilemap(Vec2(), "tilemap/TESTMAP.json")

        self.player = Entity()
        self.player.add_component(PositionComponent(Vec2(10, 10)))
        self.player.add_component(SpriteComponent("images/idle.png")).scale = 0.2
        self.player.add_component(PhysicsComponent())
        self.player.add_component(ControlComponent(ControlType.CLASSICJUMP))

        self.esys.add_entity(self.tilemap)
        self.esys.add_entity(self.player)

        self.run()

    def add_progressbar(self):
        self.progress.value += 5


Game()
