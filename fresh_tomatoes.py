#!/usr/bin/env python
import webbrowser
import os
import re
# Styles and scripting for the page
mainHeadPage = '''
<!DOCTYPE html>
<html>
<head >
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Movie trailers</title>
   <style>
.modal{
    display: none;
    position: fixed;
    z-index: 1;
    padding-top:30px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
}
.modal-content {
    position:relative;
    margin: 10% auto;
    padding: 30px;
    width: 60%;
    min-height:330px;
}
.close {
    position:absolute;
    top:0;
    right:22%;
    margin:auto;
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}
.close:hover,
.close:focus {
    background-color: rgb(255,0,0);
    text-decoration: none;
    cursor: pointer;
    padding-left:1px;
    padding-right:1px;
}
      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      div.s1:hover{
             border:1px;
             background-color:blue;
             border-radius:200px;
             }
       div.s2:hover{
             border:1px;
             background-color:red;
             border-radius:200px;
             }
       div.s3:hover{
             border:1px;
             background-color:indigo;
             border-radius:200px;
             }
       div.s4:hover{
             border:1px;
             background-color:green;
             border-radius:200px;
             }
       div.s5:hover{
             border:1px;
             background-color:skyblue;
             border-radius:200px;
             }
       div.s6:hover{
             border:1px;
             background-color:MediumSeaGreen;
             border-radius:200px;
             }
       .s1{width:33%;}
       .s2{width:34%;}
       .s3{width:33%;}
       .s4{width:33%;}
       .s5{width:34%;}
       .s6{width:33%;}
        }
      h1 {
         font-family:arial,cursive;
         width:auto;
         }
        p{
        position:center;
        background-color:MediumSeaGreen;
        width:100%;
        }
     .t
         {
         border:2px;
         border-radius:200px;
         }
         }
      </style>
      <div>
      <!-- The Modal -->
         <div id="myModal" class="modal">
  <!-- Modal content -->
           <div class="modal-content">
                <span class="close">&times;</span>
             <center><iframe id="v" style="width:60%" height="330px"
                      src="" frameborder="0" allow="autoplay; encrypted-media"
                      allowfullscreen></iframe></center>
          </div>
        </div>
</div>
       <script>
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("v").setAttribute("src",c);
}
    span.onclick = function() {
        document.getElementById("v").src=document.getElementById("v").src;
        modal.style.display = "none";
}
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>
</head>
'''
mainContentPage = '''
<body style="text-align:center">
  <center><div class="p"> <h1 style="color:blue">MOVIE TRAILERS</h1>
   </center></div>
   <div class="container">
   <div class="box s1" onclick="onc('nda6eGtu8DI')"> <img vspace="30"
   src="https://bit.ly/2x0Oa2q" style="width:60%"height="400"  class="t">
   <h2 style="color:white;">RESUGURRAM</h2></div>
   <div class="box s2" onclick="onc('b6TQ4tWGiPI')"> <img vspace="30"
   src="https://bit.ly/2rXN2Xz" style="width:60%"height="400"  class="t">
   <h2 style="color:white;">MYSTERY</h2></div>
   <div class="box s3" onclick="onc('10r9ozshGVE')"> <img vspace="30"
   src="https://bit.ly/2rWPNJD" style="width:60%" height="400" class="t">
   <h2 style="color:white;">KUNG FU PANDA 3</h2>  </div>
   <div class="box s4" onclick="onc('i5qOzqD9Rms')"> <img vspace="30"
   src="https://bit.ly/2rYfr0o" style="width:60%"height="400"  class="t">
   <h2 style="color:white;">INCREDIBLES</h2></div>
   <div class="box s5" onclick="onc('fa2RZf0m39g')"> <img vspace="30"
   src="https://bit.ly/2ICRc2s" style="width:60%" height="400" class="t">
   <h2 style="color:white;">SPY NEXTDOOR</h2>  </div>
   <div class="box s6" onclick="onc('2DEJTRwuEi4')"> <img vspace="30"
   src="https://bit.ly/2IUmzol" style="width:60%" height="400" class="t">
   <h2 style="color:white;">FIZA</h2></div>
</body>
</html>
'''
movieTileContent = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
  data-trailer-youtube-id="{trailer_youtube_id}"
  data-toggle="modal" data-target="#trailer">
<img src="{poster_image_url}"width="220" height="342">
<h2 style="color:white;">{movie_title}</h2>
</div>
'''


def createMovieTilesContent(movies):

    sai = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
              r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0)
                              if youtube_id_match
                              else None)
        sai+= movieTileContent.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return sai


def open_movies_page(movies):
    # Create or overwrite the output file

    output_file = open('fresh_tomatoes.htm', 'w')
    # Replace the movie tiles placeholder generated content
    rendered_content = mainContentPage.format(
        movie_tile=createMovieTilesContent(movies))
    # Output the file
    output_file.write(mainHeadPage + rendered_content)
    output_file.close()
    # Open the output file in the default browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
