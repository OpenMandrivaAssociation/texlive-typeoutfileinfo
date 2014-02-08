# revision 26313
# category Package
# catalog-ctan /support/typeoutfileinfo
# catalog-date 2012-03-16 14:12:34 +0100
# catalog-license lppl1.3
# catalog-version 0.1a
Name:		texlive-typeoutfileinfo
Version:	0.1a
Release:	3
Summary:	Display class/package/file information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/typeoutfileinfo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeoutfileinfo.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/typeoutfileinfo/typeoutfileinfo.sh typeoutfileinfo
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1a-2
+ Revision: 813134
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1a-1
+ Revision: 787811
- Import texlive-typeoutfileinfo
- Import texlive-typeoutfileinfo

