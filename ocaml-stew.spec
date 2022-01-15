#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A stew of OCaml utility function
Summary(pl.UTF-8):	Zbiór funkcji narzędziowych dla OCamla
Name:		ocaml-stew
Version:	0.12.0
Release:	23
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://raevnos.pennmush.org/code/stew-%{version}.tar.gz
# Source0-md5:	7e822ca90a5265a2f1b94e81add6eb4c
URL:		http://raevnos.pennmush.org/code/ocaml.html
BuildRequires:	autoconf
BuildRequires:	ocaml >= 1:3.09.2
BuildRequires:	ocaml-findlib >= 0.7.2
BuildRequires:	ocaml-pcre-devel
%requires_eq	ocaml-pcre
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stew is a general-purpose library of useful utility and extension
routines. Highlights include random number generators and
distributions, locale support, improved time printing, and character
classification routines that are locale-dependant.

This package contains files needed to run bytecode executables using
this library.

%description -l pl.UTF-8
Stew jest ogólnego użytku biblioteką użytecznych funkcji narzędziowych
i rozszerzeń. Zawiera generatory i dystrybucje liczb losowych,
wsparcie dla lokalizacji, ulepszone drukowanie czasu, oraz funkcje
klasyfikacji znaków (<ctype.h>), które są zależne od locale.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package devel
Summary:	A stew of OCaml utility function - development part
Summary(pl.UTF-8):	Zbiór funkcji narzędziowych dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Stew is a general-purpose library of useful utility and extension
routines. Highlights include random number generators and
distributions, locale support, improved time printing, and character
classification routines that are locale-dependant.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Stew jest ogólnego użytku biblioteką użytecznych funkcji narzędziowych
i rozszerzeń. Zawiera generatory i dystrybucje liczb losowych,
wsparcie dla lokalizacji, ulepszone drukowanie czasu, oraz funkcje
klasyfikacji znaków (<ctype.h>), które są zależne od locale.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q -n stew-%{version}

%build
%{__autoconf}
%configure
%{__make} all %{?with_ocaml_opt:opt}
rm -f *.cma
%{__make} DLL='-cclib -lstew'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs

%{__make} install \
	CAMLLIB=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/*.so.owner

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllstew.so
%dir %{_libdir}/ocaml/stew
%{_libdir}/ocaml/stew/META
%{_libdir}/ocaml/stew/*.cma

%files devel
%defattr(644,root,root,755)
%doc html/*
%{_libdir}/ocaml/stew/libstew.a
%{_libdir}/ocaml/stew/*.cmi
%{_libdir}/ocaml/stew/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/stew/stew.a
%{_libdir}/ocaml/stew/*.cmx
%{_libdir}/ocaml/stew/*.cmxa
%endif
