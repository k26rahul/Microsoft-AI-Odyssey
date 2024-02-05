from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces
# Import namespaces
import azure.ai.vision as sdk


def main():

  global cv_client

  try:
    # Get Configuration Settings
    load_dotenv()
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')

    # Authenticate Azure AI Vision client
    # Authenticate Azure AI Vision client
    cv_client = sdk.VisionServiceOptions(ai_endpoint, ai_key)

    # Menu for text reading functions
    print('\n1: Use Read API for image (Lincoln.jpg)\n2: Read handwriting (Note.jpg)\nAny other key to quit\n')
    command = input('Enter a number:')
    if command == '1':
      image_file = os.path.join('images', 'Lincoln.jpg')
      GetTextRead(image_file)
    elif command == '2':
      image_file = os.path.join('images', 'Note.jpg')
      GetTextRead(image_file)

  except Exception as ex:
    print(ex)


def GetTextRead(image_file):
  print('\n')

  # Use Analyze image function to read text in image
  # Use Analyze image function to read text in image
  print('Reading text in {}\n'.format(image_file))

  analysis_options = sdk.ImageAnalysisOptions()

  features = analysis_options.features = (
      # Specify the features to be retrieved
      # Specify features to be retrieved
      sdk.ImageAnalysisFeature.TEXT
  )

  # Get image analysis
  image = sdk.VisionSource(image_file)

  image_analyzer = sdk.ImageAnalyzer(cv_client, image, analysis_options)

  result = image_analyzer.analyze()

  if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

      # Get image captions
    if result.text is not None:
      print("\nText:")

      # Prepare image for drawing
      image = Image.open(image_file)
      fig = plt.figure(figsize=(image.width/100, image.height/100))
      plt.axis('off')
      draw = ImageDraw.Draw(image)
      color = 'cyan'

      for line in result.text.lines:
        # Return the text detected in the image
        # Return the text detected in the image
        print(line.content)

        drawLinePolygon = True

        r = line.bounding_polygon
        bounding_polygon = ((r[0], r[1]), (r[2], r[3]),
                            (r[4], r[5]), (r[6], r[7]))

        # Return each line detected in the image and the position bounding box around each line
        # Return each line detected in the image and the position bounding box around each line
        print(" Line: '{}', Bounding Polygon: {}".format(
            line.content, bounding_polygon))

        # Return each word detected in the image and the position bounding box around each word with the confidence level of each word
        # Return each word detected in the image and the position bounding box around each word with the confidence level of each word
        for word in line.words:
          r = word.bounding_polygon
          bounding_polygon = ((r[0], r[1]), (r[2], r[3]),
                              (r[4], r[5]), (r[6], r[7]))
          print("  Word: '{}', Bounding Polygon: {}, Confidence: {}".format(
              word.content, bounding_polygon, word.confidence))

          # Draw word bounding polygon
          drawLinePolygon = False
          draw.polygon(bounding_polygon, outline=color, width=3)

        # Draw line bounding polygon
        if drawLinePolygon:
          draw.polygon(bounding_polygon, outline=color, width=3)

      # Save image
      plt.imshow(image)
      plt.tight_layout(pad=0)
      outputfile = 'text.jpg'
      fig.savefig(outputfile)
      print('\n  Results saved in', outputfile)


if __name__ == "__main__":
  main()
