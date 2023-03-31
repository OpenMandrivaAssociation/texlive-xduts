Name:		texlive-xduts
Version:	64124
Release:	2
Summary:	Xidian University TeX Suite
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xduts
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
XDUTS is designed to help Xidian University students use LaTeX
typesetting efficiently. XDUTS contains a font configuration
package that meets the school's requirements and can be applied
to any document class. In addition, there are thesis and thesis
proposal templates for both undergraduate and postgraduate that
meet the school's requirements.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/xduts
%{_texmfdistdir}/tex/xelatex/xduts
%doc %{_texmfdistdir}/doc/xelatex/xduts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
