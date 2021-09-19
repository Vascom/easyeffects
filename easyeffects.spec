Name:           easyeffects
Version:        6.1.1
Release:        1%{?dist}
Summary:        Audio effects for PipeWire applications

License:        GPLv3+
Url:            https://github.com/wwmm/easyeffects
Source0:        %url/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Provides:       pulseeffects = 5.0.4-3
Obsoletes:      pulseeffects < 5.0.4-3

BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  boost-devel >= 1.70
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  zita-convolver-devel >= 3.1.0
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(nlohmann_json)

BuildRequires:  cmake

Requires:       hicolor-icon-theme
Requires:       dbus-common
#Requires:       ladspa-swh-plugins >= 0.4
Requires:       lv2-calf-plugins >= 0.90.0
Requires:       ladspa-calf-plugins
Requires:       lv2-mdala-plugins
Requires:       lsp-plugins-lv2

Recommends:     zam-plugins
Recommends:     lv2-zam-plugins
Recommends:     ladspa-zam-plugins
Recommends:     rubberband


%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PipeWire applications.

%prep
%autosetup
# Downgrade lv2 dependency version
sed -i 's|1.18.2|1.18.0|' src/meson.build

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
--dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}

# Change absolute symlinks to relative
# https://github.com/wwmm/pulseeffects/issues/590
find %{buildroot}%{_datadir}/help/ -type l -exec bash -c 'ln -sf ../../../C/easyeffects/figures/$(basename {}) {}' \;


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%{_datadir}/help/*/%{name}
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service


%changelog
* Sun Sep 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.1-1
- Initial packaging
