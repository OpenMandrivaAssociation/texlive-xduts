%global tl_name xduts
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.2.7.2
Release:	%{tl_revision}.1
Summary:	Xidian University TeX Suite
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xduts
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xduts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
XDUTS is designed to help Xidian University students use LaTeX
typesetting efficiently. XDUTS contains a font configuration package
that meets the school's requirements and can be applied to any document
class. In addition, there are thesis and thesis proposal templates for
both undergraduate and postgraduate that meet the school's requirements.

