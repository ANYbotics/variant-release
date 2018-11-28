Name:           ros-melodic-variant-topic-test
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS variant_topic_test package

Group:          Development/Libraries
License:        GNU Lesser General Public License (LGPL)
URL:            http://github.com/ethz-asl/ros-topic-variant
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-variant-msgs
Requires:       ros-melodic-variant-topic-tools
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-variant-msgs
BuildRequires:  ros-melodic-variant-topic-tools

%description
Variant topic tools testing suites.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Nov 28 2018 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Wed Nov 21 2018 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

