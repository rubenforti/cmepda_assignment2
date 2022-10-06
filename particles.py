#!/usr/bin/env python
# Copyright (C) 2022 r.forti1@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Second assignment for the CMEPDA course, 2022/23."""

# --- Goal
# Write a program to explore the properties of a few elementary Particles.
# The program must contain a Base class Particle and two Child classes, Proton
# and Alpha, that inherit from it.

# --- Specifications
# - instances of the class Particle must be initialized with their mass,
#   charge, and name
# - the class constructor must also accept (optionally) and store one and only
#   one of the following quantities: energy, momentum, beta or gamma
# - whatever the choice, the user should be able to read and set any of the
#   above mentioned quantities using just the '.' (dot) operator e.g.
#   print(my_particle.energy), my_particle.beta = 0.5
# - attempts to set non physical values should be rejected
# - the Particle class must have a method to print the Particle information in
#   a formatted way
# - the child classes Alpha and Protons must use class attributes to store
#   their mass, charge and name

import math


class Particle:
    """ Class representing a generic particle - storing beta and mass
    """

    def __init__(self, beta, mass, charge=0, name=""):
        if beta < 1 and beta > 0 and mass > 0:
            self._beta = float(beta)
            self._mass = float(mass)  # in MeV
        else:
            print("ERROR: non physical values inserted")
            self._beta = float("nan")
            self._mass = float("nan")

    @property
    def beta(self):
        return self._beta

    @property
    def mass(self):
        return self._mass

    @property
    def gamma(self):
        return 1/math.sqrt(1-(self.beta**2))

    @property
    def energy(self):
        """ Return the energy of the particle in MeV/c^2 """
        return self.mass*self.gamma

    @property
    def momentum(self):
        """ Return the momentum of the particle in MeV/c """
        return self.mass*self.beta*self.gamma

    @beta.setter
    def beta(self, beta):
        if abs(beta) < 1.:
            self._beta = beta
        else:
            print(
                "ERROR: speed is greater than c! are you studying a Tachyon?")

    @gamma.setter
    def gamma(self, new_gamma):
        if new_gamma > 1.:
            self.beta = math.sqrt((new_gamma**2)-1)/new_gamma
        else:
            print(
                "ERROR: speed is greater than c! are you studying a Tachyon?")

    @energy.setter
    def energy(self, new_energy):
        self.beta = math.sqrt(1-(self.mass**2/new_energy**2))

    @momentum.setter
    def momentum(self, new_momentum):
        x = new_momentum/self.mass
        self.beta = x/math.sqrt(1+(x**2))

    def properties(self):
        print("Particle properties:")
        print(f" - Speed = {self.beta:.3f} c")
        print(f" - Gamma factor = {self.gamma:.3f}")
        print(f" - Energy = {self.energy:.3f} MeV/c^2")
        print(f" - Momentum = {self.momentum:.3f} MeV/c")
        print(" ")


class Alpha(Particle):
    def __init__(self, beta):
        m = 3738  # MeV
        Particle.__init__(self, beta, m)
        self._charge = 2.
        self._name = "Alpha"

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name


class Proton(Particle):
    def __init__(self, beta):
        m = 937.3  # MeV
        Particle.__init__(self, beta, m)
        self._charge = 1.
        self._name = "Proton"

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    al = Proton(0.9)
    al.properties()
