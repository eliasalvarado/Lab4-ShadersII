

vertexShader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec2 uvs;
out vec3 outPosition;
out vec3 outNormals;

void main() {
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1);
    uvs = texCoords;
    outNormals = (modelMatrix * vec4(normals, 0)).xyz;
    outPosition = position;
}

'''

fragmentShader = '''
#version 450 core

layout (binding = 0) uniform sampler2D tex;

uniform vec3 directionalLight;

in vec2 uvs;
in vec3 outNormals;

out vec4 fragColor;

void main() {
    float intensity = dot(outNormals, -directionalLight);
    intensity = min(1, intensity);
    intensity = max(0, intensity);
    fragColor = texture(tex, uvs) * intensity;
}

'''


pruebaShader = '''
#version 450 core

layout (binding = 0) uniform sampler2D tex;

uniform vec3 directionalLight;
uniform float time;

in vec2 uvs;
in vec3 outNormals;
in vec3 outPosition;

out vec4 fragColor;

vec3 color() {
  
  vec3 color = vec3(0.0, 0.0, 0.0);
  
  if( abs(mod(abs(outPosition.x), abs(0.2 * sin(time * 0.5)))) < 0.1){
    color.x = 1.0;
  }

  return color;
}

void main() {
    fragColor = vec4(color(), 1);
}

'''
