%global debug_package %{nil}
%global commit e173f2617262664901039e3c821929afce05d2c1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20241018
%global tag 1
%global ver_count 1

Name:           vk-hdr-layer
Version:        %{tag}
Release:        %{git_date}.%{ver_count}.%{shortcommit}%{?dist}
Summary:        Vulkan layer utilizing a small color management / HDR protocol for experimentation
License:        MIT
URL:            https://github.com/Zamundaaa/VK_hdr_layer
Source:         %{url}/archive/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(vkroots)

%description
%{name} is a vulkan layer utilizing a small color management / HDR protocol for experimentation

%prep
%autosetup -n VK_hdr_layer-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/*
%{_libdir}/*.so
