Name:		texlive-emarks
Version:	24504
Release:	1
Summary:	Named mark registers with e-TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emarks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emarks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
E-TeX provides 32 768 mark registers; using this facility is
far more comfortable than LaTeX tricks with \markright,
\markboth, \leftmark and \rightmark. The package provides two
commands for marking: \marksthe and \marksthecs, which have *
forms which disable expansion; new mark registers are allocated
as needed. Syntax is closely modelled on the \marks primitive.
Four commands are provided for retrieving the marks registers'
content: \thefirstmarks, \thebotmarks, thetopmarks and
\getthemarks; and the command \ifmarksequal is available for
comparing the content of marks registers. The package requires
an e-TeX-enabled engine, and the etex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emarks/emarks.sty
%doc %{_texmfdistdir}/doc/latex/emarks/Fingerprint.jpg
%doc %{_texmfdistdir}/doc/latex/emarks/README
%doc %{_texmfdistdir}/doc/latex/emarks/emarks-fingerprint.png
%doc %{_texmfdistdir}/doc/latex/emarks/emarks.pdf
#- source
%doc %{_texmfdistdir}/source/latex/emarks/emarks.drv
%doc %{_texmfdistdir}/source/latex/emarks/emarks.dtx
%doc %{_texmfdistdir}/source/latex/emarks/emarks.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
