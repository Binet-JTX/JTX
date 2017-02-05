from videos.models import Video, Proj, Relation_proj, Category

def importer(filename, category = "A trier", proj = "A trier 2015"):
    c = Category.objects.get_or_create(titre=category)[0]
    p = Proj.objects.get_or_create(titre=proj, category=c)[0]
    f = open(filename)
    for x in f.read().splitlines():
        false_title = x.split('/')[-1].split('.')[-2].split('_')
        title = ' '.join(false_title)
        if len(false_title) > 1:
            title = ' '.join(false_title[1:])
        v = Video(titre=title, url=x)
        print "Creating {}, {}".format(title, x)
        v.save()
        r = Relation_proj(proj=p, video=v)
        r.save()
