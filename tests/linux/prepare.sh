cd linux
sudo apt update
# You can add libraries that were nesessary to compile the kernel on your machine
sudo apt install -y wget build-essential libncurses-dev gawk flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf llvm
make defconfig
make clean
