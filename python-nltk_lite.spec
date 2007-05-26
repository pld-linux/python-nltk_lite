
%define	module	nltk_lite

Summary:	Natural Language Toolkit
Name:		python-%{module}
Version:	0.7.5
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/nltk/nltk_lite-%{version}.tar.gz
# Source0-md5:	eece3cdf514c049051599ec3983b7186
URL:		http://nltk.sourceforge.net/
%pyrequires_eq	python
BuildRequires:	python-devel
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Langauge Toolkit (NLTK-Lite) is a Python package for
processing natural language text. It was developed as a simpler,
lightweight version of NLTK.

%prep
%setup  -q -n %{module}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
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
