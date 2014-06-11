# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND polyblocks_sources
)

add_library(gnuradio-polyblocks SHARED ${polyblocks_sources})
target_link_libraries(gnuradio-polyblocks ${Boost_LIBRARIES} ${GRUEL_LIBRARIES} ${GNURADIO_CORE_LIBRARIES})
set_target_properties(gnuradio-polyblocks PROPERTIES DEFINE_SYMBOL "gnuradio_polyblocks_EXPORTS")

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-polyblocks
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_polyblocks_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_polyblocks.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_polyblocks.cc
)

add_executable(test-polyblocks ${test_polyblocks_sources})

target_link_libraries(
  test-polyblocks
  ${GNURADIO_CORE_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-polyblocks
)

GR_ADD_TEST(test_polyblocks test-polyblocks)
