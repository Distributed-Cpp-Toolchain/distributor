cd linux
sudo apt update
# You can add libraries that were nesessary to compile the kernel on your machine
sudo apt install -y flex bison
make defconfig
make clean
