from OpenGL.GL import *
import bridge_api
import gl_utils
import glfw
import cv2

device = bridge_api.get_device(0)
quilt_image_count = device.quilt.tiling_dimension_x * device.quilt.tiling_dimension_y

window_title = 'looking_glass_rendering_python_api'
# vert = device.shader.vertex_shader
# frag = device.shader.fragment_shader

vertex_shader_code = """
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

void main() {
    gl_Position = vec4(aPos, 1.0);
    TexCoord = aTexCoord;
}
"""

fragment_shader_code = """
#version 330 core
out vec4 FragColor;
in vec2 TexCoord;

uniform sampler2D ourTexture;

void main() {
    FragColor = texture(ourTexture, TexCoord);
}
"""

def create_window():
    window = glfw.create_window(device.window.w, device.window.h, window_title, None, None)
    glfw.set_window_pos(window, device.window.x, device.window.y)
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")
    return window


def render_loop(window, VAO, shader_program):
    cv_image = cv2.imread('test_data/quilt_test.png')
    texture_id = gl_utils.load_texture_from_cv_image(cv_image)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

        glfw.swap_buffers(window)
        glfw.poll_events()


def main():
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")
    window = create_window()
    glfw.make_context_current(window)

    VAO = gl_utils.setup_vertex_data()
    shader_program = gl_utils.create_shader_program(vertex_shader_code, fragment_shader_code)
    render_loop(window, VAO, shader_program)

    glfw.terminate()


def _generate_lenticular_projection(quilt):
    lent = 0
    return lent

def _generate_quilt_from_rgbd(rgb_depth):
    # quilt_image_count
    quilt = 0
    return quilt




def show_lenticular_projection(lent):
    pass

def show_quilt(quilt):
    # lent = _generate_lenticular_projection(quilt)
    # show_lenticular_projection(lent)
    pass

def show_rgb_depth(rgb_depth):
    # quilt = _generate_quilt_from_rgbd(rgb_depth)
    # show_quilt(quilt)
    pass


if __name__ == "__main__":
    main()
