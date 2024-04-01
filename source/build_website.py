import os
import shutil

from build_textbox import textbox_parse

PAGES_DIR = "./pages"
OUTPUT_DIR = "../"
SITE_NAME = "jonathanjulou.github.io/"

PRE_PATH = "./pre.html"
POST_PATH = "./post.html"

# copy css and mdl license
shutil.copy("./MDL License", OUTPUT_DIR)
shutil.copy("./styles.css", OUTPUT_DIR)

#PAGES = list(os.listdir(PAGES_DIR))
PAGES = {"index.md": "Home",
         "music.md": "Music",
         "drawing.md": "Drawings",
         "about.md": "About"}


def parse_md(md_txt):
    body = '<main class="mdl-layout__content">\n'
    intextbox = False
    textbox_buf = ''

    for line in md_txt.split("\n"):
        if line.startswith("//"):
            continue

        if intextbox and not line.startswith("[endtextbox]"):
            textbox_buf += line + "\n"
            continue

        # handle layout markers
        if line.startswith("["):
            if line.startswith("[startgrid]"):
                body += '<div class="mdl-grid portfolio-max-width">'
                continue

            if line.startswith("[endgrid]"):
                body += '</div>'
                continue

            if line.startswith("[starttextbox]"):
                textbox_buf = ''
                intextbox = True
                continue

            if line.startswith("[endtextbox]"):
                intextbox = False
                body += textbox_parse(textbox_buf)
                continue

            if line.startswith("[imagebox]"):
                image_path = line.split("(")[1].split(")")[0]
                with open("./imagebox.html", "r") as f_in:
                    imagebox_html = f_in.read().replace("IMAGE_PATH", image_path)
                body += imagebox_html
                continue

            if line.startswith("[videobox]"):
                video_path = line.split("(")[1].split(")")[0]
                with open("./videobox.html", "r") as f_in:
                    videobox_html = f_in.read().replace("VIDEO_PATH", video_path)
                body += videobox_html
                continue

    return body+"</main>\n"


if __name__ == "__main__":
    for page in PAGES:
        page_path = os.path.join(PAGES_DIR, page)
        output_path = os.path.join(OUTPUT_DIR, page.replace(".md", ".html"))

        # copy header from prelude file
        with open(PRE_PATH, "r") as f_in:
            with open(output_path, "w") as f_out:
                header = f_in.read()

                # adjust the navigation manu un the header
                navigation = ""
                for other_page in PAGES:
                    if other_page == page:
                        navigation += '<a class="mdl-navigation__link is-active" href="{}">{}</a>'.format(page.replace(".md", ".html"), PAGES[page])
                    else:
                        navigation += '<a class="mdl-navigation__link" href="{}">{}</a>'.format(other_page.replace(".md", ".html"), PAGES[other_page])

                header = header.replace("NAVIGATION", navigation)

                f_out.write(header)


        # fill the body of the page by translating the markdown
        with open(page_path, "r") as f_in:
            with open(output_path, "a") as f_out:
                f_out.write(parse_md(f_in.read()))

        # copy footer from postlude file
        with open(POST_PATH, "r") as f_in:
            with open(output_path, "a") as f_out:
                f_out.write(f_in.read())
