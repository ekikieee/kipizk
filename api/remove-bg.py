from http.server import BaseHTTPRequestHandler
import json
import base64
import io
from PIL import Image
from rembg import remove

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # CORS headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        try:
            # Read request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Parse JSON
            data = json.loads(post_data.decode('utf-8'))
            image_data = data.get('image')
            
            if not image_data:
                raise ValueError('No image data provided')
            
            # Decode base64 image
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            
            # Open image
            input_image = Image.open(io.BytesIO(image_bytes))
            
            # Remove background
            output_image = remove(input_image)
            
            # Convert to PNG bytes
            output_buffer = io.BytesIO()
            output_image.save(output_buffer, format='PNG')
            output_bytes = output_buffer.getvalue()
            
            # Encode to base64
            output_base64 = base64.b64encode(output_bytes).decode('utf-8')
            
            # Send response
            response = {
                'success': True,
                'image': f'data:image/png;base64,{output_base64}'
            }
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            error_response = {
                'success': False,
                'error': str(e)
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
