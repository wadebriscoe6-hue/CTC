"""
Interactive Kinetic Caption, Sticker & Video Player Component
Renders an animated HTML5 video player simulation with word-by-word subtitles,
clickable AI B-Roll overlays, and animated viral stickers (Follow, Double Tap, VVS Diamond, Fire).
"""

import json
from typing import List, Dict, Any, Optional

def get_caption_player_html(
    clip_title: str, 
    subtitles: List[Any], 
    caption_style: str = "Matrix Neon Green", 
    position: str = "bottom",
    broll_info: Optional[Dict[str, Any]] = None,
    placed_stickers: Optional[List[Dict[str, Any]]] = None
) -> str:
    subs_data = []
    for s in subtitles:
        subs_data.append({
            "word": getattr(s, "word", str(s)),
            "start": getattr(s, "start", 0.0),
            "end": getattr(s, "end", 1.0),
            "is_keyword": getattr(s, "is_keyword", False),
            "color": getattr(s, "highlight_color", "#00FF66")
        })

    subs_json = json.dumps(subs_data)
    
    stks_data = []
    if placed_stickers:
        for p in placed_stickers:
            stk_obj = p.get("sticker", {})
            stks_data.append({
                "badge_text": stk_obj.get("badge_text", "💎 CLOTH TALK"),
                "style": stk_obj.get("style", "background: #00FF66; color: #000;"),
                "start_time": p.get("start_time", 0.0),
                "end_time": p.get("end_time", 4.0),
                "position": p.get("position", "top-right")
            })
    stks_json = json.dumps(stks_data)

    pos_style = "bottom: 45px;"
    if position == "center": pos_style = "top: 50%; transform: translateY(-50%);"
    elif position == "top": pos_style = "top: 60px;"

    glow_color = "#00FF66"
    if "Gold" in caption_style or "Hormozi" in caption_style: glow_color = "#FFD700"
    elif "Cyan" in caption_style: glow_color = "#00F0FF"
    elif "Pink" in caption_style or "Purple" in caption_style: glow_color = "#EC4899"

    broll_title = broll_info.get("title", "AI B-Roll Overlay") if broll_info else "No B-Roll Attached"
    broll_icon = broll_info.get("visual_icon", "🎥") if broll_info else "🎙️"
    broll_desc = broll_info.get("description", "Standard speaker view") if broll_info else "Standard speaker framing"
    has_broll = "true" if broll_info else "false"

    template = """
    <div style="background: #020617; border: 2px solid __GLOW_COLOR__; border-radius: 24px; padding: 16px; max-width: 320px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.9), 0 0 20px __GLOW_COLOR__40;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 11px; font-weight: bold; color: __GLOW_COLOR__;">👑 ClothTalk AI Video Suite</span>
            <span style="font-size: 10px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; color: #94A3B8;">9:16 Vertical HD</span>
        </div>

        <div id="video-screen" style="width: 100%; height: 420px; background: radial-gradient(circle at center, #1e293b, #090d16); border-radius: 18px; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid rgba(255,255,255,0.08);">
            
            <div style="padding: 12px; display: flex; align-items: center; justify-content: space-between; z-index: 2;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="width: 28px; height: 28px; border-radius: 50%; background: #00FF66; color: #000; font-weight: 900; font-size: 12px; display: flex; align-items: center; justify-content: center;">CT</div>
                    <div>
                        <div style="font-size: 12px; font-weight: bold; color: #FFFFFF;">@clothtalk88</div>
                        <div style="font-size: 9px; color: #94A3B8;">Original Audio &bull; Cloth Talk</div>
                    </div>
                </div>
                <div id="broll-status-badge" style="font-size: 9px; background: rgba(0,255,102,0.15); color: #00FF66; border: 1px solid #00FF66; border-radius: 10px; padding: 2px 6px;">
                    B-ROLL: ACTIVE
                </div>
            </div>

            <div id="sticker-container" style="position: absolute; top: 52px; left: 12px; right: 12px; z-index: 4; pointer-events: none; text-align: center; transition: all 0.3s ease;">
                <div id="active-sticker-badge" style="display: none; font-size: 11px; margin: 0 auto; width: fit-content; transform: scale(1.05);"></div>
            </div>

            <div id="visual-center" style="text-align: center; margin-top: 15px; z-index: 1; padding: 0 12px;">
                <div id="broll-card" style="background: rgba(15, 23, 42, 0.85); border: 1.5px solid __GLOW_COLOR__; border-radius: 12px; padding: 12px; margin-bottom: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.6); transition: all 0.3s ease;">
                    <div id="broll-icon-elem" style="font-size: 36px; margin-bottom: 4px; filter: drop-shadow(0 0 10px __GLOW_COLOR__);">__BROLL_ICON__</div>
                    <div id="broll-title-elem" style="font-size: 11px; font-weight: bold; color: #FFFFFF; text-transform: uppercase;">__BROLL_TITLE__</div>
                    <div id="broll-desc-elem" style="font-size: 9px; color: #94A3B8; margin-top: 2px;">__BROLL_DESC__</div>
                </div>
            </div>

            <div id="caption-overlay" style="position: absolute; left: 10px; right: 10px; __POS_STYLE__ text-align: center; z-index: 3; padding: 10px 14px; background: rgba(2, 6, 23, 0.88); border-radius: 14px; border: 1.5px solid __GLOW_COLOR__; backdrop-filter: blur(8px); box-shadow: 0 4px 20px rgba(0,0,0,0.8);">
                <div id="active-words-container" style="font-family: 'Impact', 'Arial Black', sans-serif; font-size: 18px; line-height: 1.4; text-transform: uppercase; color: #FFFFFF; letter-spacing: 0.5px;">
                    Loading auto-generated captions...
                </div>
            </div>

            <div style="padding: 10px 12px; z-index: 2; background: linear-gradient(transparent, rgba(0,0,0,0.8));">
                <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94A3B8; margin-bottom: 4px;">
                    <span id="current-time-display">0.0s</span>
                    <span id="total-time-display">0.0s</span>
                </div>
                <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.2); border-radius: 2px; overflow: hidden;">
                    <div id="playback-bar" style="width: 0%; height: 100%; background: __GLOW_COLOR__; transition: width 0.1s linear;"></div>
                </div>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; align-items: center; margin-top: 12px;">
            <button id="btn-play-pause" style="background: __GLOW_COLOR__; color: #000; border: none; font-weight: bold; font-size: 12px; padding: 6px 16px; border-radius: 20px; cursor: pointer;">▶ Play 9:16 Video</button>
            <button id="btn-restart" style="background: rgba(255,255,255,0.1); color: #FFF; border: 1px solid rgba(255,255,255,0.2); font-size: 11px; padding: 6px 12px; border-radius: 20px; cursor: pointer;">🔄 Restart</button>
        </div>
    </div>

    <script>
    (function() {
        const subs = __SUBS_JSON__;
        const stickers = __STKS_JSON__;
        if (!subs || subs.length === 0) return;

        const totalDuration = subs[subs.length - 1].end - subs[0].start || 15.0;
        const startTime = subs[0].start;
        let currentTime = 0;
        let isPlaying = false;
        let playInterval = null;

        const container = document.getElementById('active-words-container');
        const playBtn = document.getElementById('btn-play-pause');
        const restartBtn = document.getElementById('btn-restart');
        const progressBar = document.getElementById('playback-bar');
        const curTimeDisp = document.getElementById('current-time-display');
        const totTimeDisp = document.getElementById('total-time-display');
        const brollCard = document.getElementById('broll-card');
        const brollBadge = document.getElementById('broll-status-badge');
        const stickerBadge = document.getElementById('active-sticker-badge');

        if (totTimeDisp) totTimeDisp.innerText = totalDuration.toFixed(1) + 's';

        function updateCaptions(timeOffset) {
            const absoluteTime = startTime + timeOffset;
            
            let activeIdx = -1;
            for (let i = 0; i < subs.length; i++) {
                if (absoluteTime >= subs[i].start && absoluteTime <= subs[i].end) {
                    activeIdx = i;
                    break;
                }
            }

            if (activeIdx === -1) {
                for (let i = 0; i < subs.length; i++) {
                    if (absoluteTime < subs[i].start) {
                        activeIdx = i;
                        break;
                    }
                }
                if (activeIdx === -1) activeIdx = subs.length - 1;
            }

            const windowStart = Math.max(0, activeIdx - 1);
            const windowEnd = Math.min(subs.length, activeIdx + 3);
            const currentChunk = subs.slice(windowStart, windowEnd);

            let html = '';
            currentChunk.forEach(item => {
                const isActive = (absoluteTime >= item.start && absoluteTime <= item.end);
                if (isActive) {
                    const kwGlow = item.is_keyword ? 'background: rgba(0,255,102,0.25); border-radius: 4px; padding: 0 4px;' : '';
                    html += '<span style="color: __GLOW_COLOR__; font-size: 21px; text-shadow: 0 0 14px __GLOW_COLOR__; transform: scale(1.1); display: inline-block; ' + kwGlow + '">' + item.word + '</span> ';
                } else if (item.is_keyword) {
                    html += '<span style="color: __GLOW_COLOR__; text-shadow: 0 0 8px __GLOW_COLOR__80;">' + item.word + '</span> ';
                } else {
                    html += '<span style="color: #94A3B8;">' + item.word + '</span> ';
                }
            });

            if (container) container.innerHTML = html;
            if (curTimeDisp) curTimeDisp.innerText = timeOffset.toFixed(1) + 's';
            if (progressBar) progressBar.style.width = ((timeOffset / totalDuration) * 100) + '%';
            
            if (brollCard) {
                if (timeOffset <= 4.5 && __HAS_BROLL__) {
                    brollCard.style.borderColor = '__GLOW_COLOR__';
                    brollCard.style.boxShadow = '0 0 20px __GLOW_COLOR__60';
                    if (brollBadge) brollBadge.style.display = 'block';
                } else {
                    brollCard.style.borderColor = 'rgba(255,255,255,0.1)';
                    brollCard.style.boxShadow = 'none';
                }
            }

            if (stickerBadge && stickers && stickers.length > 0) {
                let currentStk = null;
                for (let k = 0; k < stickers.length; k++) {
                    if (timeOffset >= stickers[k].start_time && timeOffset <= stickers[k].end_time) {
                        currentStk = stickers[k];
                        break;
                    }
                }
                if (currentStk) {
                    stickerBadge.style.display = 'block';
                    stickerBadge.innerText = currentStk.badge_text;
                    stickerBadge.setAttribute('style', currentStk.style + ' display: block; margin: 0 auto; width: fit-content; font-size: 11px;');
                } else {
                    stickerBadge.style.display = 'none';
                }
            }
        }

        function play() {
            isPlaying = true;
            if (playBtn) playBtn.innerText = '⏸ Pause';
            playInterval = setInterval(() => {
                currentTime += 0.05;
                if (currentTime >= totalDuration) currentTime = 0;
                updateCaptions(currentTime);
            }, 50);
        }

        function pause() {
            isPlaying = false;
            if (playBtn) playBtn.innerText = '▶ Play 9:16 Video';
            clearInterval(playInterval);
        }

        if (playBtn) playBtn.addEventListener('click', () => { if (isPlaying) pause(); else play(); });
        if (restartBtn) restartBtn.addEventListener('click', () => { currentTime = 0; updateCaptions(0); if (!isPlaying) play(); });

        updateCaptions(0);
        setTimeout(play, 400);
    })();
    </script>
    """

    return (
        template.replace("__GLOW_COLOR__", glow_color)
        .replace("__POS_STYLE__", pos_style)
        .replace("__SUBS_JSON__", subs_json)
        .replace("__STKS_JSON__", stks_json)
        .replace("__BROLL_TITLE__", broll_title)
        .replace("__BROLL_ICON__", broll_icon)
        .replace("__BROLL_DESC__", broll_desc)
        .replace("__HAS_BROLL__", has_broll)
    )

def render_interactive_caption_player(
    clip_title: str, 
    subtitles: List[Any], 
    caption_style: str = "Matrix Neon Green", 
    position: str = "bottom",
    broll_info: Optional[Dict[str, Any]] = None,
    placed_stickers: Optional[List[Dict[str, Any]]] = None
):
    try:
        import streamlit.components.v1 as components
        html_code = get_caption_player_html(clip_title, subtitles, caption_style, position, broll_info, placed_stickers)
        components.html(html_code, height=540, scrolling=False)
    except Exception:
        pass
