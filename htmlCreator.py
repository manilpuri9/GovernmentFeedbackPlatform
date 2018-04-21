import webbrowser
import os
import re

main_page_head = '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="device-width, initial-scale=1">
    <title>Dashboard</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
        <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
        <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
        <link rel="stylesheet" type="text/css" href="css/util.css">
        <link rel="stylesheet" type="text/css" href="css/main.css">
    <style type="text/css" media="screen">
        
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .title-fonts{
            font-size: 3rem;
            font-weight: 400;
            line-height: 1.5;
        }
        .title-dimention{
            height: 40%;
            width:30%;
            background-color: rgb(26, 7, 7);
            border: #0b1606;
            margin:15px;
        }
        @media screen and (max-width: 300px) {
          .title-dimention{
              height: 40%;
              width: 200px;
              background-color: rgb(26, 7, 7);
              border: #0b1606;
              margin:15px;
          }
        }

        @media screen and (max-width: 990px) {
          .title-dimention{
              height: 40%;
              width: 50%;
              background-color: rgb(26, 7, 7);
              border: #0b1606;
              margin:auto;
              align-self: center;
              margin-bottom: 10px;
          }
        }
        .bgs{
            background: -webkit-linear-gradient(45deg, #56ab2f, #a8e063);
            background: -o-linear-gradient(45deg, #56ab2f, #a8e063);
            background: -moz-linear-gradient(45deg, #56ab2f, #a8e063);
            background: linear-gradient(45deg, #56ab2f, #a8e063)";
        }
        .pad{
            padding-top:  50px;
        }
        .zoom {transition: transform .2s;}
    .zoom:hover {
        -ms-transform: scale(1.5); /* IE 9 */
        -webkit-transform: scale(1.5); /* Safari 3-8 */
        transform: scale(1.1); 
    }
    </style>
</head>
'''


main_page_content = '''
    <!DOCTYPE html>
<html lang="en">
  <body class="bg-contact3" style="background-image: url('static/images/bg-01.jpg');background-repeat: no-repeat;
    background-attachment: fixed;">

    <!-- Main Page Content -->
    <div class="container bgs">
      <div class="navbar navbar-inverse navbar-fixed-top bgs" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <center><a class="navbar-brand" href="#">Dashboard</a></center>
          </div>
        </div>
      </div>
    </div>
    <div class="container pad">
      {problem_tiles}
    </div>
  </body>
</html>
'''

problem_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center title-dimention bgs zoom" style="position:relative" id="4KPTXpQehio" data-toggle="modal" data-target="#">
    <span class="title-fonts">{title}</span>
    <p id ="description">{details}</p>
    <p id ="catagory pull-right">{category}</p>
    <span class="pull-left"id="urgency">{level}</span>
    <button  class="btn btn-default pull-right " id="vote">UPVOTE</button>
</div>

'''

def create_problem_tiles_content(problems):

    content = ''
    for problem in problems:

        content += problem_tile_content.format(
            title = problem.title,
            details = problem.details,
            category = problem.category,
            level = problem.level
        )
    return content

def hc(problems):
    output_file = open("dashboardTrial.html","w")

    rendered_content = main_page_content.format(problem_tiles=create_problem_tiles_content(problems))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    return main_page_head + rendered_content
#   # Output the file
#   output_file.write(main_page_head + rendered_content)
#   output_file.close()

#   # open the output file in the browser
#   url = os.path.abspath(output_file.name)
#   webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
