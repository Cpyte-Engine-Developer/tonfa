docker build --tag=kivy/buildozer .
docker run --interactive --tty --rm \
    --volume "$HOME/.buildozer":/home/user/.buildozer \
    --volume "$PWD":/home/user/hostcwd \
    kivy/buildozer android release

zipalign -v 4 bin/tonfa-0.0.2-arm64-v8a-release-unsigned.apk bin/tonfa-0.0.2-arm64-v8a-release-signed.apk
apksigner sign --ks ~/keystores/tonfa.keystore --ks-key-alias tonfa bin/tonfa-0.0.2-arm64-v8a-release-signed.apk
