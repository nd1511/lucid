# Copyright 2018 The Lucid Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from __future__ import absolute_import, division, print_function

import tensorflow as tf
import math

def rand_select(xs, seed=None):
    rand_n = tf.random_uniform((), 0, len(xs), "int32", seed=seed)
    return tf.constant(xs)[rand_n]


def angle2rads(angle, unit):
    angle = tf.cast(angle, "float32")
    if unit.lower() in ["degrees", "degs", "deg"]:
        angle = math.pi * angle / 180.
    elif unit.lower() in ["radians", "rads", "rad"]:
        angle = angle
    return angle


def compose(transforms):
    def inner(x):
        for transform in transforms:
            x = transform(x)
        return x

    return inner
