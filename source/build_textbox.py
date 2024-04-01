def textbox_parse(md_content):
    body = '<div class="mdl-grid portfolio-max-width">\n'
    body += '<div class="mdl-cell mdl-cell--12-col mdl-card mdl-shadow--4dp">\n'

    for line in md_content.split("\n"):

        if line.startswith('#####'):
            body += '<h6 class="mdl-cell mdl-cell--12-col">{}</h6>\n'.format(line.split("#####")[1])
            continue

        if line.startswith('####'):
            body += '<h5 class="mdl-cell mdl-cell--12-col">{}</h5>\n'.format(line.split("####")[1])
            continue

        if line.startswith('###'):
            body += '<h3 class="mdl-cell mdl-cell--12-col mdl-typography--headline">{}</h3>\n'.format(line.split("###")[1])
            continue

        if line.startswith('##'):
            body += '<div class="mdl-card__title">\n<h2 class="mdl-card__title-text">{}</h2>\n</div>\n'.format(line.split("##")[1])
            continue

        if line.startswith('#'):
            body += '<div class="mdl-card__title">\n<h1 class="mdl-card__title-text">{}</h1>\n</div>\n'.format(line.split("#")[1])
            continue

        if line.startswith("[image]"):
            image_path = line.split("(")[1].split(")")[0]
            body += '<div class="mdl-card__media">\n<img class="article-image" src=" {}" border="0" alt="">\n</div>'.format(image_path)
            continue

        if line.startswith("[video]"):
            image_path = line.split("(")[1].split(")")[0]
            body += '<div class="video-card mdl-card__media">\n<video controls><source src=" {}" type="video/mp4">Your browser does not support the video tag.</video>\n</div>'.format(image_path)
            continue

        if line.startswith("[startgrid]"):
            body += '<div class="mdl-grid portfolio-copy">\n'
            continue

        if line.startswith("[endgrid]"):
            body += '</div>\n'
            continue

        if line.startswith("[startparagraph]"):
            body += '<div class="mdl-cell mdl-cell--8-col mdl-card__supporting-text no-padding ">\n'
            continue

        if line.startswith("[endparagraph]"):
            body += '</div>\n'
            continue

        if line == "":
            body += '<br>'
            continue


        body += '{}\n'.format(line)

    return body+"</div>\n"+"</div>\n"
