#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-UsingR
Version  : 2.0.6
Release  : 2
URL      : https://cran.r-project.org/src/contrib/UsingR_2.0-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/UsingR_2.0-6.tar.gz
Summary  : Data Sets, Etc. for the Text "Using R for Introductory
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Hmisc
BuildRequires : R-HistData
BuildRequires : R-Hmisc
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
textbook "Using R for Introductory Statistics," second
    edition.

%prep
%setup -q -c -n UsingR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571952738

%install
export SOURCE_DATE_EPOCH=1571952738
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library UsingR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library UsingR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library UsingR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc UsingR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/UsingR/DESCRIPTION
/usr/lib64/R/library/UsingR/INDEX
/usr/lib64/R/library/UsingR/Meta/Rd.rds
/usr/lib64/R/library/UsingR/Meta/data.rds
/usr/lib64/R/library/UsingR/Meta/features.rds
/usr/lib64/R/library/UsingR/Meta/hsearch.rds
/usr/lib64/R/library/UsingR/Meta/links.rds
/usr/lib64/R/library/UsingR/Meta/nsInfo.rds
/usr/lib64/R/library/UsingR/Meta/package.rds
/usr/lib64/R/library/UsingR/NAMESPACE
/usr/lib64/R/library/UsingR/NEWS
/usr/lib64/R/library/UsingR/R/UsingR
/usr/lib64/R/library/UsingR/R/UsingR.rdb
/usr/lib64/R/library/UsingR/R/UsingR.rdx
/usr/lib64/R/library/UsingR/answers/print-answers.pdf
/usr/lib64/R/library/UsingR/answers/problem-1.10.html
/usr/lib64/R/library/UsingR/answers/problem-1.16.html
/usr/lib64/R/library/UsingR/answers/problem-1.17.html
/usr/lib64/R/library/UsingR/answers/problem-1.19.html
/usr/lib64/R/library/UsingR/answers/problem-1.24.html
/usr/lib64/R/library/UsingR/answers/problem-1.27.html
/usr/lib64/R/library/UsingR/answers/problem-1.5.html
/usr/lib64/R/library/UsingR/answers/problem-1.6.html
/usr/lib64/R/library/UsingR/answers/problem-1.7.html
/usr/lib64/R/library/UsingR/answers/problem-1.9.html
/usr/lib64/R/library/UsingR/answers/problem-10.1.html
/usr/lib64/R/library/UsingR/answers/problem-10.11.html
/usr/lib64/R/library/UsingR/answers/problem-10.13.html
/usr/lib64/R/library/UsingR/answers/problem-10.16.html
/usr/lib64/R/library/UsingR/answers/problem-10.20.html
/usr/lib64/R/library/UsingR/answers/problem-10.21.html
/usr/lib64/R/library/UsingR/answers/problem-10.25.html
/usr/lib64/R/library/UsingR/answers/problem-10.27.html
/usr/lib64/R/library/UsingR/answers/problem-10.29.html
/usr/lib64/R/library/UsingR/answers/problem-10.6.html
/usr/lib64/R/library/UsingR/answers/problem-10.9.html
/usr/lib64/R/library/UsingR/answers/problem-11.1.html
/usr/lib64/R/library/UsingR/answers/problem-11.10.html
/usr/lib64/R/library/UsingR/answers/problem-11.12.html
/usr/lib64/R/library/UsingR/answers/problem-11.14.html
/usr/lib64/R/library/UsingR/answers/problem-11.16.html
/usr/lib64/R/library/UsingR/answers/problem-11.18.html
/usr/lib64/R/library/UsingR/answers/problem-11.19.html
/usr/lib64/R/library/UsingR/answers/problem-11.22.html
/usr/lib64/R/library/UsingR/answers/problem-11.25.html
/usr/lib64/R/library/UsingR/answers/problem-11.26.html
/usr/lib64/R/library/UsingR/answers/problem-11.28.html
/usr/lib64/R/library/UsingR/answers/problem-11.3.html
/usr/lib64/R/library/UsingR/answers/problem-11.6.html
/usr/lib64/R/library/UsingR/answers/problem-12.1.html
/usr/lib64/R/library/UsingR/answers/problem-12.10.html
/usr/lib64/R/library/UsingR/answers/problem-12.8.html
/usr/lib64/R/library/UsingR/answers/problem-12.9.html
/usr/lib64/R/library/UsingR/answers/problem-2.12.html
/usr/lib64/R/library/UsingR/answers/problem-2.13.html
/usr/lib64/R/library/UsingR/answers/problem-2.14.html
/usr/lib64/R/library/UsingR/answers/problem-2.17.html
/usr/lib64/R/library/UsingR/answers/problem-2.19.html
/usr/lib64/R/library/UsingR/answers/problem-2.20.html
/usr/lib64/R/library/UsingR/answers/problem-2.22.html
/usr/lib64/R/library/UsingR/answers/problem-2.34.html
/usr/lib64/R/library/UsingR/answers/problem-2.35.html
/usr/lib64/R/library/UsingR/answers/problem-2.39.html
/usr/lib64/R/library/UsingR/answers/problem-2.45.html
/usr/lib64/R/library/UsingR/answers/problem-2.5.html
/usr/lib64/R/library/UsingR/answers/problem-2.9.html
/usr/lib64/R/library/UsingR/answers/problem-3.10.html
/usr/lib64/R/library/UsingR/answers/problem-3.12.html
/usr/lib64/R/library/UsingR/answers/problem-3.14.html
/usr/lib64/R/library/UsingR/answers/problem-3.17.html
/usr/lib64/R/library/UsingR/answers/problem-3.2.html
/usr/lib64/R/library/UsingR/answers/problem-3.21.html
/usr/lib64/R/library/UsingR/answers/problem-3.24.html
/usr/lib64/R/library/UsingR/answers/problem-3.25.html
/usr/lib64/R/library/UsingR/answers/problem-3.28.html
/usr/lib64/R/library/UsingR/answers/problem-3.3.html
/usr/lib64/R/library/UsingR/answers/problem-3.30.html
/usr/lib64/R/library/UsingR/answers/problem-3.32.html
/usr/lib64/R/library/UsingR/answers/problem-3.33.html
/usr/lib64/R/library/UsingR/answers/problem-3.4.html
/usr/lib64/R/library/UsingR/answers/problem-3.7.html
/usr/lib64/R/library/UsingR/answers/problem-3.9.html
/usr/lib64/R/library/UsingR/answers/problem-4.1.html
/usr/lib64/R/library/UsingR/answers/problem-4.10.html
/usr/lib64/R/library/UsingR/answers/problem-4.12.html
/usr/lib64/R/library/UsingR/answers/problem-4.15.html
/usr/lib64/R/library/UsingR/answers/problem-4.16.html
/usr/lib64/R/library/UsingR/answers/problem-4.17.html
/usr/lib64/R/library/UsingR/answers/problem-4.2.html
/usr/lib64/R/library/UsingR/answers/problem-4.22.html
/usr/lib64/R/library/UsingR/answers/problem-4.25.html
/usr/lib64/R/library/UsingR/answers/problem-4.27.html
/usr/lib64/R/library/UsingR/answers/problem-4.3.html
/usr/lib64/R/library/UsingR/answers/problem-4.5.html
/usr/lib64/R/library/UsingR/answers/problem-4.6.html
/usr/lib64/R/library/UsingR/answers/problem-5.10.html
/usr/lib64/R/library/UsingR/answers/problem-5.12.html
/usr/lib64/R/library/UsingR/answers/problem-5.16.html
/usr/lib64/R/library/UsingR/answers/problem-5.19.html
/usr/lib64/R/library/UsingR/answers/problem-5.21.html
/usr/lib64/R/library/UsingR/answers/problem-5.27.html
/usr/lib64/R/library/UsingR/answers/problem-5.28.html
/usr/lib64/R/library/UsingR/answers/problem-5.3.html
/usr/lib64/R/library/UsingR/answers/problem-5.30.html
/usr/lib64/R/library/UsingR/answers/problem-5.9.html
/usr/lib64/R/library/UsingR/answers/problem-6.10.html
/usr/lib64/R/library/UsingR/answers/problem-6.2.html
/usr/lib64/R/library/UsingR/answers/problem-6.3.html
/usr/lib64/R/library/UsingR/answers/problem-6.4.html
/usr/lib64/R/library/UsingR/answers/problem-6.5.html
/usr/lib64/R/library/UsingR/answers/problem-6.7.html
/usr/lib64/R/library/UsingR/answers/problem-7.11.html
/usr/lib64/R/library/UsingR/answers/problem-7.13.html
/usr/lib64/R/library/UsingR/answers/problem-7.15.html
/usr/lib64/R/library/UsingR/answers/problem-7.17.html
/usr/lib64/R/library/UsingR/answers/problem-7.18.html
/usr/lib64/R/library/UsingR/answers/problem-7.22.html
/usr/lib64/R/library/UsingR/answers/problem-7.24.html
/usr/lib64/R/library/UsingR/answers/problem-7.27.html
/usr/lib64/R/library/UsingR/answers/problem-7.29.html
/usr/lib64/R/library/UsingR/answers/problem-7.31.html
/usr/lib64/R/library/UsingR/answers/problem-7.32.html
/usr/lib64/R/library/UsingR/answers/problem-7.5.html
/usr/lib64/R/library/UsingR/answers/problem-7.8.html
/usr/lib64/R/library/UsingR/answers/problem-8.1.html
/usr/lib64/R/library/UsingR/answers/problem-8.12.html
/usr/lib64/R/library/UsingR/answers/problem-8.16.html
/usr/lib64/R/library/UsingR/answers/problem-8.17.html
/usr/lib64/R/library/UsingR/answers/problem-8.18.html
/usr/lib64/R/library/UsingR/answers/problem-8.2.html
/usr/lib64/R/library/UsingR/answers/problem-8.21.html
/usr/lib64/R/library/UsingR/answers/problem-8.27.html
/usr/lib64/R/library/UsingR/answers/problem-8.28.html
/usr/lib64/R/library/UsingR/answers/problem-8.35.html
/usr/lib64/R/library/UsingR/answers/problem-8.5.html
/usr/lib64/R/library/UsingR/answers/problem-8.6.html
/usr/lib64/R/library/UsingR/answers/problem-8.9.html
/usr/lib64/R/library/UsingR/answers/problem-9.11.html
/usr/lib64/R/library/UsingR/answers/problem-9.13.html
/usr/lib64/R/library/UsingR/answers/problem-9.17.html
/usr/lib64/R/library/UsingR/answers/problem-9.19.html
/usr/lib64/R/library/UsingR/answers/problem-9.20.html
/usr/lib64/R/library/UsingR/answers/problem-9.3.html
/usr/lib64/R/library/UsingR/answers/problem-9.7.html
/usr/lib64/R/library/UsingR/data/Rdata.rdb
/usr/lib64/R/library/UsingR/data/Rdata.rds
/usr/lib64/R/library/UsingR/data/Rdata.rdx
/usr/lib64/R/library/UsingR/data/datalist
/usr/lib64/R/library/UsingR/errata/errata.html
/usr/lib64/R/library/UsingR/errata/errata.md
/usr/lib64/R/library/UsingR/errata/runErrata.R
/usr/lib64/R/library/UsingR/help/AnIndex
/usr/lib64/R/library/UsingR/help/UsingR.rdb
/usr/lib64/R/library/UsingR/help/UsingR.rdx
/usr/lib64/R/library/UsingR/help/aliases.rds
/usr/lib64/R/library/UsingR/help/paths.rds
/usr/lib64/R/library/UsingR/html/00Index.html
/usr/lib64/R/library/UsingR/html/R.css
/usr/lib64/R/library/UsingR/samplecode/analysis-of-variance.R
/usr/lib64/R/library/UsingR/samplecode/bivariate.R
/usr/lib64/R/library/UsingR/samplecode/confidence-intervals.R
/usr/lib64/R/library/UsingR/samplecode/extensions-of-linear-model.R
/usr/lib64/R/library/UsingR/samplecode/goodness-of-fit.R
/usr/lib64/R/library/UsingR/samplecode/linear-regression.R
/usr/lib64/R/library/UsingR/samplecode/multivariate-graphics.R
/usr/lib64/R/library/UsingR/samplecode/multivariate.R
/usr/lib64/R/library/UsingR/samplecode/populations.R
/usr/lib64/R/library/UsingR/samplecode/significance-tests.R
/usr/lib64/R/library/UsingR/samplecode/statistical-inference.R
/usr/lib64/R/library/UsingR/samplecode/univariate.R
/usr/lib64/R/library/UsingR/shiny/bw-selection/README.md
/usr/lib64/R/library/UsingR/shiny/bw-selection/server.R
/usr/lib64/R/library/UsingR/shiny/bw-selection/ui.R
/usr/lib64/R/library/UsingR/shiny/hist-bins/README.md
/usr/lib64/R/library/UsingR/shiny/hist-bins/server.R
/usr/lib64/R/library/UsingR/shiny/hist-bins/ui.R
/usr/lib64/R/library/UsingR/shiny/mean-influence/server.R
/usr/lib64/R/library/UsingR/shiny/mean-influence/ui.R
/usr/lib64/R/library/UsingR/shiny/startup.R
/usr/lib64/R/library/UsingR/tsEx/nytimes.R
