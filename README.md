# Analysis-of-flow-in-a-stenosed-aorta
<p align="justify">
Investigation of a simulation of laminar incompressible flow through a stenosis of the aorta using varying orders of discretisation. From the data obtained, the fine, medium and coarse mesh types were compared graphically and qualitatively.
</p>

<p align="center">
<img width="607" alt="Screen Shot 2021-12-22 at 12 44 56 PM" src="https://user-images.githubusercontent.com/70657426/147080609-845699fa-23e3-4724-bae2-77e35b011511.png">
 </p>

<p align="justify">
The figure displays the velocity profiles below the stenosis for all mesh types and order of accuracy. The x-axis represents the position of the flow in relationship with the centre of the vessel located at X = 0 meter. The zero velocity points refers to the boundaries/walls of the vessels, experiencing no-slip condition and hence no velocity (viscous flow).
 </p>
 
<p align="center">
  
![V](https://user-images.githubusercontent.com/70657426/147080849-cf8cbbb4-d1bd-46cf-ac46-9780ecec2472.png)
  
</p>

<p align="justify">
The figure below displays the pressure drop profiles for all mesh types and order of accuracy at each iteration. The plot was cropped as the profile remains unchanged for the rest of the iterations, staying stable at the same pressure value.
 </p>
 
![PD](https://user-images.githubusercontent.com/70657426/147081942-ad3e1a76-b90a-4f55-92e3-5e4afe91316b.png)

<p align="justify">
The two figures below show a comparison of the velocity and pressure profiles for two meshes. We can see the velocity profile contains no significant differences. This might be because differences in mesh quality are not as important for the velocity profile as compared to the level of mesh or order of simulation used. Pressure drop is a bit more sensitive to mesh quality, with the medium mesh showing a smoother pressure profile than the initial mesh due to the presence of more AV/truncation error in the medium mesh. 
 </p>
 
![V2](https://user-images.githubusercontent.com/70657426/147083585-5c7f5bb4-9136-451b-8fc1-c5f9d8e861d7.png)

![PD2](https://user-images.githubusercontent.com/70657426/147083631-653e5943-4ee1-40a8-8e80-19e2e8e7d4d0.png)
