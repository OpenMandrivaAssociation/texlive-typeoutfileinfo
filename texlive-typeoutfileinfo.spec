Name:		texlive-typeoutfileinfo
Version:	29349
Release:	1
Summary:	Display class/package/file information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/typeoutfileinfo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-typeoutfileinfo.bin = %{EVRD}

%description
The package provides a minimalist shell script, for Unix
systems, that displays the information content in a
\ProvidesFile, \ProvidesPackage or \ProvidesClass command in a
LaTeX source file. The package requires that the readprov
package is available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/typeoutfileinfo
%{_texmfdistdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh
%doc %{_texmfdistdir}/doc/support/typeoutfileinfo/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh typeoutfileinfo
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
