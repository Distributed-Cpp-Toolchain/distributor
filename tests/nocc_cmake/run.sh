# Building
ROOT=$(pwd)/../..

rm -rf build
mkdir build
cd build
if [ -f "/usr/bin/clang++" ]; then
  cmake -DCMAKE_CXX_COMPILER_LAUNCHER=$ROOT/cucc -DCMAKE_CXX_COMPILER=/usr/bin/clang++ ..
else
  cmake -DCMAKE_CXX_COMPILER_LAUNCHER=$ROOT/cucc ..
fi

# Compiling:
make -j4
