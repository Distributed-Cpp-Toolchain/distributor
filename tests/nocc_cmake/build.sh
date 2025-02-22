rm -rf build
mkdir build
cd build
if [ -f "/usr/bin/clang++" ]; then
  cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++ ..
else
  cmake ..
fi
make -j4
