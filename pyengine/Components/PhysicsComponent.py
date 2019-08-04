from pyengine.Components import PositionComponent, SpriteComponent
from pyengine.Utils import Vec2
import pygame
import math
import pymunk

__all__ = ["PhysicsComponent"]


class PhysicsComponent:
    def __init__(self, affectbygravity: bool = True, friction: float = .5, elasticity: float = .5, mass: int = 1,
                 callback=None):
        self.__entity = None
        self.origin_image = None
        self.body = None
        self.shape = None
        self.affectbygravity = affectbygravity
        self.friction = friction
        self.elasticity = elasticity
        self.mass = mass
        self.callback = callback

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity
        self.origin_image = entity.image
        temp = entity.rect.width
        vc = [(0, temp), (temp, temp), (temp, 0), (0, 0)]
        moment = pymunk.moment_for_box(self.mass, (entity.rect.width, entity.rect.height))
        self.body = pymunk.Body(self.mass, moment)
        self.body.center_of_gravity = (temp/2, temp/2)
        if not self.affectbygravity:
            self.body.body_type = self.body.KINEMATIC
        self.shape = pymunk.Poly(self.body, vc)
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        if entity.has_component(PositionComponent):
            self.update_pos(entity.get_component(PositionComponent).position.coords)

    def flipy(self, pos):
        return [pos[0], -pos[1] + 640]

    def add_callback(self):
        if self.callback is not None:
            cb = self.entity.system.world.space.add_wildcard_collision_handler(self.entity.identity)
            cb.begin = self.callback

    def update(self):
        self.entity.image = pygame.transform.rotate(self.origin_image, math.degrees(self.body.angle))

        if self.entity.has_component(PositionComponent):
            print(self.flipy(self.body.position), self.entity.get_component(PositionComponent).position)
            self.entity.get_component(PositionComponent).position = Vec2(self.flipy(self.body.position))

    def update_pos(self, pos):
        self.body.position = self.flipy(pos)


