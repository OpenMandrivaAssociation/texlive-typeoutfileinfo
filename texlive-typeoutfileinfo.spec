%global tl_name typeoutfileinfo
%global tl_revision 67526
%global tl_bin_links typeoutfileinfo:%{_texmfdistdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.32
Release:	%{tl_revision}.1
Summary:	Display class/package/file information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/typeoutfileinfo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fileinfo)
Requires:	texlive(typeoutfileinfo.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a minimalist shell script, for Unix systems, that
displays the information content in a \ProvidesFile, \ProvidesPackage or
\ProvidesClass command in a LaTeX source file. The package requires that
the readprov package is available.

