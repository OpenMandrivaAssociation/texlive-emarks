%global tl_name emarks
%global tl_revision 24504

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Named mark registers with e-TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emarks
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
E-TeX provides 32 768 mark registers; using this facility is far more
comfortable than LaTeX tricks with \markright, \markboth, \leftmark and
\rightmark. The package provides two commands for marking: \marksthe and
\marksthecs, which have * forms which disable expansion; new mark
registers are allocated as needed. Syntax is closely modelled on the
\marks primitive. Four commands are provided for retrieving the marks
registers' content: \thefirstmarks, \thebotmarks, thetopmarks and
\getthemarks; and the command \ifmarksequal is available for comparing
the content of marks registers. The package requires an e-TeX-enabled
engine, and the etex package.

