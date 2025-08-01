
%define	module	nltk_lite

Summary:	Natural Language Toolkit
Summary(pl.UTF-8):	Przybornik obsługi języków naturalnych (Natural Language Toolkit)
Name:		python-%{module}
Version:	0.7.5
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/nltk/nltk_lite-%{version}.tar.gz
# Source0-md5:	eece3cdf514c049051599ec3983b7186
Patch0:		%{name}-no-similarity.patch
URL:		http://nltk.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Language Toolkit (NLTK-Lite) is a Python module for
processing natural language text. It was developed as a simpler,
lightweight version of NLTK.

%description -l pl.UTF-8
Natural Language Toolkit (NLTK-Lite) jest modułem języka Python
przetwarzającym tekst w języku naturalnym. Został on stworzony
jako prostsza, lekka wersja NLTK.

%prep
%setup  -q -n %{module}-%{version}
%patch -P0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{py_sitescriptdir}/*
