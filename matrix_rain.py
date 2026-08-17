"""
Matrix Digital Rain & Cyber Pattern Component
Injects a lightweight HTML5 Canvas green digital matrix rain
with cyber glyphs, diamonds, and Cloth Talk 88 matrix streams.
"""

def get_matrix_rain_html() -> str:
    return """
    <div id="matrix-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: -1; opacity: 0.18;">
        <canvas id="matrix-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
    </div>
    <script>
    (function() {
        const canvas = document.getElementById('matrix-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resize();
        window.addEventListener('resize', resize);

        const chars = '01CLOTHTALK88JARVISDIAMOND💎0123456789ABCDEF01';
        const fontSize = 14;
        let columns = Math.floor(canvas.width / fontSize);
        let drops = Array(columns).fill(1);

        function draw() {
            ctx.fillStyle = 'rgba(11, 15, 25, 0.08)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#00FF66';
            ctx.font = fontSize + 'px monospace';

            for (let i = 0; i < drops.length; i++) {
                const text = chars.charAt(Math.floor(Math.random() * chars.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 33);
    })();
    </script>
    """

def inject_matrix_rain():
    try:
        import streamlit.components.v1 as components
        components.html(get_matrix_rain_html(), height=0, width=0)
    except Exception:
        pass
