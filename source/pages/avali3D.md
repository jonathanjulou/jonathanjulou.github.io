[starttextbox]

[image](images/projects/avali3D/Sanstitre.jpg)

[startgrid]
###Avali 3D model + rig
[startparagraph]

This project was made over the course of almost a year in Blender, going from concept to sculpting to retopology to texturing and procedural materials and finally rigging and animating.


[endparagraph]
[startparagraph]
####Concept
The idea was to make a 3D model based on the Avali open species by RyuujinZero (<a href=https://avali.fandom.com/wiki/Art_%26_Concepts>https://avali.fandom.com/wiki/Art_%26_Concepts</a>) that would be as photorealistic as possible with my skills, as a way to improve on them.


A lot of drawings were made to understand how to build similar 2D forms from basic 3D shapes on paper. This one resembles the most the final outcome and was an inspiration to one of the animations:


[endparagraph]
[endgrid]
[endtextbox]

[startgrid]
[imagebox](images/projects/avali3D/20230913_093120.jpg)
[endgrid]

[starttextbox]
[startgrid]
[startparagraph]
####3D model
After sculpting using drawings as references, a retopology of the mesh was made manually. There are many automatic retopology tools that work well for hard surfaces and static objects, but for an animated character, topology has to follow the planned deformations, for example giving more edge loops on the elbows to plan for extension, while following the angle of rotation to avoid shearing artifacts.


The hardest part is the face to account for the eyes and mouth, as well as the four ears. In the end the ears were kept as separate objects for ease of rigging, the intersection being hidden by the helmet anyways.


After the retopology of the main body, the armor was modeled directly on top by extruding parts of the body topology or layering planes on top with the shrinkwrap modifier. Some elements like the gun and the pouch were made separately, but still with direct low-poly modeling.


I found going high-poly to low poly with retopology to work the best for organic shapes, to keep freedom of shape at sculpting stage, and then applying good topology on the pre-existing shape at retopo stage, so that one can focus on a single problem at a time. For hard-surface objects, low poly to high-poly was the fastest since the shapes are simpler and topology is not as important for animation.


[endparagraph]
[endgrid]
[endtextbox]

[startgrid]
[imagebox](images/projects/avali3D/topo3.jpg)
[imagebox](images/projects/avali3D/topo4.jpg)
[endgrid]
[startgrid]
[imagebox](images/projects/avali3D/topo1.jpg)
[imagebox](images/projects/avali3D/topo2.jpg)
[imagebox](images/projects/avali3D/topo5.jpg)
[endgrid]


[starttextbox]
[startgrid]
[startparagraph]
####Shading
Besides the feathers and some hand-painted masks, no texture was used. All shaders were achieved using noise patterns like Perlin and Voronoi in the Blender shader editor. It gives more control on the aspect of the surface and avoids having to deal with seams, but it is much harder to achieve a PBR look.


The wings look terrible compared to the rest, and were a mess to try rigging, hence why they were removed for the animations. In a future project, a feather-by-feather approach would be more appropriate rather than sticking with faking using textures.


[endparagraph]
[endgrid]
[endtextbox]

[startgrid]
[imagebox](images/projects/avali3D/untitled.jpg)
[imagebox](images/projects/avali3D/untitled2.jpg)
[imagebox](images/projects/avali3D/untitled3.jpg)
[endgrid]


[starttextbox]
[startgrid]
[startparagraph]
####Animation
Finally in parallel to the model reaching its final appearance, the IBC deadline was closing by at work, so I offered to use this personnal project for the demo.


The animation was made with said demo in mind. The idea was to have a cube in the scene, a real cube, and then show a virtual character interacting with the cube, like going on top, in fornt, behind, projecting shadows on the cube, etc...
This was to demonstrate that real-time pixel-perfect tracking was possible using mechanical encoders and a well-calibrated lens.


3 different animation cycles were keyframed by hand in blender and then exported as FBX to Unreal Engine. To interact with the cube, the virtual placeholder cube was given a holdout material in Composure, so that it still interacted with the scene ligthing and masked the character when behind, but didn't obstruct the real cube on screen.


[endparagraph]
[endgrid]
[endtextbox]

[ahtml](<div class="video-card mdl-cell mdl-shadow--4dp">)
[ahtml](<div class="mdl-card__media">)
[ahtml](<video controls><source src="images/projects/avali3D/idle20001-1250.mp4" type="video/mp4">Your browser does not support the video tag.</video>)
[ahtml](<video controls><source src="images/projects/avali3D/run0001-0180.mp4" type="video/mp4">Your browser does not support the video tag.</video>)
[ahtml](<video controls><source src="images/projects/avali3D/active0001-0383.mp4" type="video/mp4">Your browser does not support the video tag.</video>)
[ahtml](</div>)
[ahtml](</div>)

[startgrid]
[videobox](images/projects/avali3D/idle20001-1250.mp4)
[videobox](images/projects/avali3D/run0001-0180.mp4)
[videobox](images/projects/avali3D/active0001-0383.mp4)
[endgrid]

[starttextbox]
[startgrid]
[startparagraph]
### Demo at IBC
[endparagraph]
[video](images/projects/avali3D/IMG_4676.mp4)
[endgrid]
[endtextbox]
