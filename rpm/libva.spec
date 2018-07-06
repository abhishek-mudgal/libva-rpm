%define libva

Name:		libva
Version:		2.2.0
Release:		1
Summary:	Generate Your Projects

Group:		Development/Libraries
License:		MIT
URL: 		https://github.com/01org/libva.git
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext


%description
Libva is an implementation for VA-API (Video Acceleration API)

VA-API is an open-source library and API specification, which provides access to graphics hardware acceleration capabilities for video processing. It consists of a main library and driver-specific acceleration backends for each supported hardware vendor

%prep
%setup -q -n %{name}-%{version}/libva

%build
./autogen.sh --enable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%defattr(-,root,root,-)
%{_libdir}/libva/*.so.*
