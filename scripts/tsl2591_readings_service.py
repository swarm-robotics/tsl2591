#!/usr/bin/env python3
# Copyright 2022 John Harwell, All rights reserved.
#
#  This file is part of ROSBRIDGE.
#
#  ROSBRIDGE is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  ROSBRIDGE is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with
#  ROSBRIDGE.  If not, see <http://www.gnu.org/licenses/

# Core packages

# 3rd party packages
import rospy

# Project packages
import tsl2591_driver
from tsl2591.srv import ReadingsService


if __name__ == "__main__":
    rospy.init_node(__name__)
    array = tsl2591_driver.TSL2591ArrayDriver()
    s = rospy.Service('tsl2591/readings_service',
                      ReadingsService,
                      array.handle_service_request)
    print(f"{__name__}: Ready to send readings")
    rospy.spin()
