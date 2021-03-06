import numpy as np

from foolbox.attacks import GradientAttack as Attack


def test_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_attack_eps(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv, epsilons=np.linspace(0., 1., 100)[1:])
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_attack_gl(gl_bn_adversarial):
    adv = gl_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is None
    assert adv.distance.value == np.inf


def test_attack_eg(eg_bn_adversarial):
    adv = eg_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf
