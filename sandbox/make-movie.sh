rm frames/*
i=0;
for f in output/*.jpg; do
    ln -s ../$f $(printf "frames/%06d.jpg" $i);
    i=$((i+1));
done
avconv -f image2 -r 14 -i frames/%06d.jpg -i nyan.mp3 -strict experimental martian-nyan-cat.mp4
