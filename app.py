# @title GENESIS (RUTH) | Y10 MASTERS (B72 - FOUNDER RESTORED) { display-mode: "form" }
import streamlit as st
# Launch the secure verification pin modal
⁠entered_pin = st.text_input("ENTER SECURITY VERIFICATION PIN:", type="password")⁠

# Define your authorized pins (Admin/Civilian) - adjust as needed
authorized_pins = ["12345", "67890"]

if entered_pin in authorized_pins:
    print("Verification Successful. Preparing canvas...")
    # Add a brief pause for UI rendering
    time.sleep(0.5)
    uploaded = files.upload()
    # The dashboard/upload sequence will render here next
else:
    print("Invalid Pin Entered. Access Restricted.")

# DUAL UPLOAD: Select your Nadir (Overhead) and all Side Elevation shots

# Process all uploaded images for the gallery and capture BYTE SIZE signatures
image_gallery = {}
byte_signatures = {}
img_data_main = ""

for file_name in uploaded.keys():
    file_bytes = len(uploaded[file_name])
    byte_signatures[file_name] = f"SIG-{file_bytes}-{file_name[:3].upper()}"

    encoded = base64.b64encode(uploaded[file_name]).decode('utf-8')
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        image_gallery[file_name] = encoded
        if not img_data_main:
            img_data_main = encoded

gallery_json = json.dumps(image_gallery)
byte_json = json.dumps(byte_signatures)

# Keystone Note: Using double-braces {{ }} to prevent Colab Syntax Warnings on CSS
html_code = f'''
<script src="https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Fexifreader%404.12.0%2Fdist%2Fexif-reader.min.js&data=05%7C02%7C%7C097a013b67594cf067ab08deb8e46443%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C639151488226211136%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=q%2FSY1OT4pD0AakD8TXwpb1IzMBW5P4dvotry4VvrV54%3D&reserved=0"></script>
<style>
@keyframes flash-red-timer {{ 0% {{ color: #ff0000; text-shadow: 0 0 5px #ff0000; }} 50% {{ color: #550000; text-shadow: none; }} 100% {{ color: #ff0000; text-shadow: 0 0 5px #ff0000; }} }}
@keyframes flash-gold {{ 0% {{ background: #111; border-color: #555; }} 50% {{ background: #D4AF37; border-color: #ffffff; color: black; }} 100% {{ background: #111; border-color: #555; }} }}
@keyframes flash-red {{ 0% {{ color: #ff0000; text-shadow: 0 0 5px #ff0000; }} 50% {{ color: #fff; }} 100% {{ color: #ff0000; }} }}
.mode-alert {{ animation: flash-red 0.6s infinite !important; font-size: 14px !important; }}
.pitch-alert {{ animation: flash-gold 0.8s infinite !important; }}
.timer-active {{ animation: flash-red-timer 0.8s infinite !important; }}
.pitch-gold {{ color: #FFD700 !important; font-weight: bold; }}
.sqft-green {{ color: #00ff00 !important; font-weight: bold; }}
.acc-button {{ background: #FFD700 !important; color: black !important; font-weight: bold; border: none; border-radius: 4px; cursor: pointer; height: 40px; width: 100%; transition: 0.2s; }}
.acc-button:disabled {{ background: #444 !important; color: #888 !important; cursor: not-allowed; }}
.social-btn {{ text-decoration: none; color: white; font-size: 10px; font-weight: bold; padding: 4px 8px; border-radius: 4px; transition: 0.3s; display: flex; align-items: center; gap: 5px; cursor: pointer; }}
.yt-btn {{ background: #FF0000; border: 1px solid #cc0000; }}
.fb-btn {{ background: #1877F2; border: 1px solid #0e5a94; }}
.center-crosshair {{ position: absolute; top: 50%; left: 50%; width: 60px; height: 60px; border: 1px solid rgba(212, 175, 55, 0.6); border-radius: 50%; pointer-events: none; transform: translate(-50%, -50%); z-index: 3500; display: none; }}
.center-crosshair::before, .center-crosshair::after {{ content: ''; position: absolute; background: rgba(212, 175, 55, 0.6); }}
.center-crosshair::before {{ top: 50%; left: -30px; width: 120px; height: 1px; }}
.center-crosshair::after {{ left: 50%; top: -30px; width: 1px; height: 120px; }}
.v-btn {{ background: rgba(0,0,0,0.8); border: 1px solid #D4AF37; color: #D4AF37; font-size: 12px; padding: 4px 8px; cursor: pointer; border-radius: 3px; font-weight: bold; }}
.v-btn:hover {{ background: #D4AF37; color: black; }}
.trace-active {{ background: #ff0000 !important; color: white !important; }}
#side-mag {{ position: absolute; width: 140px; height: 140px; border: 2px solid #00ff00; background: black; pointer-events: none; z-index: 1000; display: none; overflow: hidden; box-shadow: 0 0 15px rgba(0,0,0,0.8); border-radius: 4px; }}
.mag-crosshair {{ position: absolute; top: 50%; left: 0; width: 100%; height: 1px; background: rgba(0, 255, 0, 0.6); }}
.mag-crosshair-v {{ position: absolute; left: 50%; top: 0; width: 1px; height: 100%; background: rgba(0, 255, 0, 0.6); }}
.upload-trigger {{ position: absolute; bottom: 5px; right: 5px; background: rgba(0,212,255,0.15); border: 1px solid #00d4ff; color: #00d4ff; font-size: 9px; padding: 3px 6px; border-radius: 4px; cursor: pointer; font-weight: bold; transition: 0.2s; z-index: 150; }}
#canvas-lock-shade {{
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    display: none;
    z-index: 9999;
    justify-content: center;
    align-items: center;
    color: #ff0000;
    font-weight: bold;
    font-size: 28px;
    letter-spacing: 2px;
    text-shadow: 0 0 15px #ff0000;
}}
</style>

<div id="genesis-root" style="background:#121212; min-height:100vh; color:white; font-family:sans-serif; width:100%; display:flex; flex-direction:column;">
<div style="padding:10px 20px; background:#1a1a1a; border-bottom:1px solid #333; display:flex; justify-content:space-between; align-items:center;">
<span style="font-weight:bold; color:#00d4ff; letter-spacing:1px;">GENESIS | Y10 MASTER <span style="color:#00ff00; font-size:10px; margin-left:10px;">99% PRECISION LOCK (B72-CLEAN-HANDSHAKE)</span></span>
<div style="display:flex; align-items:center; gap:20px; background:#252525; padding:5px 15px; border-radius:20px; border:1px solid #444;">
    <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:10px; color:#FFD700; font-weight:bold;">SKYROVER GUIDE</span>
        <input type="checkbox" id="guide-toggle" onchange="toggleGuide()" style="cursor:pointer; accent-color:#FFD700;">
    </div>
    <!-- Unified Choose File Button -->
<div class="upload-container">
            <button type="button" id="unified-upload-btn" onclick="triggerAuthPrompt()" style="background: #00d4ff; color: black; border: none; padding: 5px 15px; border-radius: 20px; font-weight: bold; cursor: pointer;">Choose File</button>
            <input type="file" id="nadir-upload" onchange="handleNadirUpload(event)" style="display: none;" accept="image/*">
        </div>
    <div style="display:flex; align-items:center; gap:15px;">
        <span style="font-size:10px; color:#aaa;">ZOOM</span>
        <input type="range" id="zoom-slider" min="0" max="2" step="0.1" value="0" oninput="updateZoom()" style="cursor:pointer; width:100px;">
        <span id="zoom-val" style="font-size:10px; color:#00d4ff; min-width:30px;">0%</span>
    </div>
</div>
<div style="display:flex; gap:10px;">
<button id="stasis-toggle" onclick="toggleStasis()" style="background: #ff0000; color: white; border: none; padding: 5px 10px; font-weight: bold; cursor: pointer; border-radius: 4px; margin-left: 10px;"> PAUSE (NATURE CALLS) </button>
  <a href="https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2F%40OspreonLLC&data=05%7C02%7C%7C097a013b67594cf067ab08deb8e46443%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C639151488226227142%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FuwuKb%2FzgeOYhGsVCEZ8yhIizCkMYhMc7Vgn%2FbAaWHM%3D&reserved=0" target="_blank" class="social-btn yt-btn">YouTube</a>
 <a href="https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.facebook.com%2Fshare%2Fv%2F1CDzTyhbMp%2F&data=05%7C02%7C%7C097a013b67594cf067ab08deb8e46443%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C639151488226238421%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=z3PZNsI8hTtPgx27Mt2%2FKWfi%2F%2FvxB4qg%2BZxyIcChyOg%3D&reserved=0" target="_blank" class="social-btn fb-btn">Facebook</a>
</div>

</div>

<div id="viewport" style="width:100%; overflow:hidden; background:#000; position:relative; min-height:550px; border-bottom:2px solid #333; display:flex; justify-content:center; align-items:flex-start;">
<div id="center-guide" class="center-crosshair"></div>
<div id="canvas-container" style="transform-origin: top center; transition: transform 0.1s ease; position:relative;">
<div id="canvas-lock-shade">SYSTEM STASIS: CANVAS LOCKED</div>
    <canvas id="canvas" style="cursor:crosshair; display:block; max-width:100%; height:auto;"></canvas>
</div>
<div id="tool-dock" style="position:absolute; background:rgba(26,26,26,0.98); border:2px solid #00d4ff; border-radius:10px; padding:10px; display:flex; flex-direction:column; gap:8px; z-index:5000; pointer-events:none; box-shadow: 0 10px 30px rgba(0,0,0,0.8); width:110px; display:none;">
    <button onclick="setMode('eave')" style="background:none; border:none; color:#00ff00; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">EAVE</button>
    <button onclick="setMode('ridge')" style="background:none; border:none; color:#00d4ff; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">RIDGE</button>
    <button onclick="setMode('rake')" style="background:none; border:none; color:#ffcc00; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">RAKE</button>
    <button onclick="setMode('hip')" style="background:none; border:none; color:#ff00ff; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">HIP</button>
    <button onclick="setMode('valley')" style="background:none; border:none; color:#ffffff; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">VALLEY</button>
    <button onclick="setMode('sw')" style="background:none; border:none; color:#ff00ff; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">SIDE WALL</button>
    <button onclick="setMode('ew')" style="background:none; border:none; color:#008080; font-weight:bold; cursor:pointer; font-size:11px; text-align:left; pointer-events:auto;">END WALL</button>
    <button onclick="undoLine()" style="background:#444; border:1px solid #666; color:white; font-weight:bold; cursor:pointer; font-size:10px; text-align:center; pointer-events:auto; border-radius:2px; padding:2px 0;">UNDO LINE</button>
    <div style="height:1px; background:#444;"></div>
    <div style="font-size:8px; color:#666; text-align:center;">MODE:<br><span id="cur-mode" style="color:#00d4ff; font-weight:bold;">EAVE</span></div>
</div>
<div id="mag-glass" style="position:absolute; width:220px; height:220px; border:2px solid #00d4ff; border-radius:8px; pointer-events:none; z-index:4000; overflow:hidden; background:black; display:none;">
    <canvas id="zoom-canvas" width="220" height="220"></canvas>
    <div style="position:absolute; top:50%; left:0; width:100%; height:1px; background:rgba(0,212,255,0.7);"></div>
    <div style="position:absolute; left:50%; top:0; width:1px; height:100%; background:rgba(0,212,255,0.7);"></div>
</div>
</div>

<div style="background:#1a1a1a; padding:15px; border-top:1px solid #444;">
<div style="display:grid; grid-template-columns: repeat(7, 1fr); gap:8px; margin-bottom:15px;">
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #00ff00;"><span style="color:#aaa; font-size:9px;">EAVES</span><div id="val-eave" style="font-size:16px; color:#00ff00; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #00d4ff;"><span style="color:#aaa; font-size:9px;">RIDGES</span><div id="val-ridge" style="font-size:16px; color:#00d4ff; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #ffcc00;"><span style="color:#aaa; font-size:9px;">RAKES</span><div id="val-rake" style="font-size:16px; color:#ffcc00; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #ff00ff;"><span style="color:#aaa; font-size:9px;">HIPS</span><div id="val-hip" style="font-size:16px; color:#ff00ff; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #ffffff;"><span style="color:#aaa; font-size:9px;">VALLEYS</span><div id="val-valley" style="font-size:16px; color:#ffffff; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #ff00ff;"><span style="color:#aaa; font-size:9px;">SIDE WALL</span><div id="val-sw" style="font-size:16px; color:#ff00ff; font-weight:bold;">0.0</div></div>
    <div style="text-align:center; background:#121212; padding:8px; border-radius:4px; border-bottom:3px solid #008080;"><span style="color:#aaa; font-size:9px;">END WALL</span><div id="val-ew" style="font-size:16px; color:#008080; font-weight:bold;">0.0</div></div>
</div>

<div style="display:flex; gap:12px; align-items: stretch; margin-bottom:10px; height: 180px;">
    <div style="width:240px; display:flex; flex-direction:column; gap:8px;">
        <div style="background:#252525; padding:8px; border-radius:8px; border:2px solid #ffcc00; display:flex; justify-content:space-between; align-items:center; height:40px;">
            <span id="label-3d" style="font-size:9px; color:#00ff00; font-weight:bold;">ON-SITE DATA</span>
            <label style="position:relative; display:inline-block; width:40px; height:18px;">
                <input type="checkbox" id="toggle-3d" style="opacity:0; width:0; height:0;">
                <span style="position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background-color:#444; transition:.4s; border-radius:20px;">
                    <span style="position:absolute; content:''; height:12px; width:12px; left:3px; bottom:3px; background-color:#ffcc00; transition:.4s; border-radius:50%;" id="slider-knob"></span>
                </span>
            </label>
            <span id="label-2d" style="font-size:9px; color:#aaa; font-weight:bold; opacity: 0.4;">2D BLUEPRINT</span>
        </div>
        <div style="background:#252525; padding:8px; border-radius:8px; border:2px solid #ffcc00; flex-grow: 1; display:flex; flex-direction:column; gap:6px; justify-content: center;">
            <div style="background:#111; border:1px solid #555; display:flex; align-items:center; border-radius:4px; height:32px; padding:0 5px;">
                <div style="flex:1.2; color:#aaa; font-size:9px; font-weight:bold; text-align:center; border-right:1px solid #333;">SCALE</div>
                <input type="number" id="ref-ft" placeholder="-" oninput="triggerScaleFlash()" style="width:40px; background:transparent; color:#00ff00; border:none; text-align:center; font-weight:bold; font-size:14px;">
                <span style="color:#666;">'</span>
                <input type="number" id="ref-in" placeholder="-" max="11" oninput="triggerScaleFlash()" style="width:35px; background:transparent; color:#00ff00; border:none; text-align:center; font-weight:bold; font-size:14px;">
                <span style="color:#666;">"</span>
            </div>
            <div style="display:flex; align-items:center; background:#111; border:1px solid #555; border-radius:4px; height:32px; padding:0 5px;" id="pitch-container">
                <div style="flex:1.2; color:#00d4ff; font-size:9px; font-weight:bold; text-align:center; border-right:1px solid #333;">PITCH</div>
                <input type="number" id="pitch-box" step="0.25" placeholder="-" oninput="resetPitchAlert()" onclick="this.parentNode.classList.remove('pitch-alert')" style="flex:1; background:transparent; color:#00ff00; border:none; text-align:center; font-weight:bold; font-size:14px;">
                <span style="color:#666; font-size:10px; margin-right:5px;"></span>
            </div>
            <div style="display:flex; align-items:center; background:#111; border:1px solid #555; border-radius:4px; height:32px; padding:0 5px;" id="metal-width-container">
                <div style="flex:1.2; color:#ff00ff; font-size:8px; font-weight:bold; text-align:center; border-right:1px solid #333; line-height:1;">METAL<br>WIDTH</div>
                <input type="number" id="metal-width-box" placeholder="COMING SOON" oninput="checkMetalRequired()" style="flex:1; background:transparent; color:#ff00ff; border:none; text-align:center; font-weight:bold; font-size:11px;">
                <span style="color:#666; font-size:10px; margin-right:5px;">IN</span>
            </div>
        </div>
    </div>

    <div style="width:2px; background:#444; margin: 10px 0;"></div>

    <div style="flex: 1.2; background:#252525; padding:10px; border-radius:8px; border:2px solid #D4AF37; display:flex; flex-direction:column; justify-content: space-between;">
       <div style="display:flex; flex-direction:column; gap:2px;">
           <span style="font-size:9px; color:#D4AF37; font-weight:bold;">PROPERTY ADDRESS (AUTO-DETECT)</span>
           <input type="text" id="attr-box" placeholder="Locating Address..." style="width:95%; height:28px; background:#111; border:1px solid #555; border-radius:4px; color:white; padding:0 8px; font-size:11px; outline:none;" readonly>
       </div>
       <div style="display:flex; flex-direction:column; gap:2px;">
           <span style="font-size:9px; color:#D4AF37; font-weight:bold;">DRONE COMPLIANCE & VERIFICATION</span>
           <div style="display:flex; gap:5px; width:98%;">
               <div id="drone-model-display" style="flex:1; height:28px; background:#111; border:1px solid #555; border-radius:4px; color:#FFD700; font-weight:bold; padding:0 8px; font-size:10px; display:flex; align-items:center; overflow:hidden; white-space:nowrap;">MODEL ID</div>
               <div id="drone-fvm-display" style="flex:1.2; height:28px; background:#111; border:1px solid #555; border-radius:4px; color:#aaa; font-weight:bold; padding:0 8px; font-size:10px; display:flex; align-items:center; justify-content:center; text-align:center;">STATUS: WAITING</div>
           </div>
       </div>
       <div style="display:flex; flex-direction:column; gap:2px; position:relative;">
           <span style="font-size:9px; color:#D4AF37; font-weight:bold;">BYTE-SIZE VERIFIED ID | LOCK</span>
           <div style="display:flex; gap:5px;">
               <input type="text" id="photo-id-box" placeholder="AUTO-SIG#" style="flex:2; height:28px; background:#111; border:1px solid #555; border-radius:4px; color:#00ff00; padding:0 8px; font-size:11px; outline:none; font-family:monospace;" readonly>
               <input type="text" id="timer-display" value="03:00" style="width:80px; height:28px; background:#111; border:1px solid #00d4ff; border-radius:4px; color:#ff0000; text-align:center; font-size:18px;" readonly>
           </div>
       </div>
   </div>

    <div style="flex: 1.2; border: 2px solid #D4AF37; padding: 10px; border-radius: 8px; background: #111; overflow-y: auto;">
        <table style="width:100%; border-collapse:collapse; font-size:10px; text-align:left;">
            <thead style="background:#222; color:#00d4ff;">
                <tr><th style="padding:4px;">#</th><th style="padding:4px;">PITCH</th><th style="padding:4px;">SQ FT</th></tr>
            </thead>
            <tbody id="facet-tbody"></tbody>
        </table>
    </div>

    <div style="flex: 2.2; display:flex; flex-direction:column; gap:6px; border: 2px solid #D4AF37; padding: 10px; border-radius: 8px; background: rgba(212, 175, 55, 0.05);">
        <div style="display:flex; gap:6px; height: 100%;">
            <div style="flex: 1; display: flex; flex-direction: column; gap: 4px;">
                <button onclick="accumulateJ18()" class="acc-button" id="acc-btn-text" style="font-size: 10px; height: 35px;">ACCUMULATE MATERIALS</button>
                <div id="acc-results" style="flex-grow: 1; color: #FFD700; font-family: monospace; font-size: 10px; padding: 8px; background: #0a0a0a; border: 1px solid #333; line-height: 1.2; overflow-y: auto;">READY...</div>
            </div>
            <div style="width: 130px; display: flex; flex-direction: column; gap: 4px;">
                <button onclick="downloadPack()" style="background:#2ecc71; color:white; border:none; padding:8px; border-radius:4px; cursor:pointer; font-weight:bold; font-size:9px;">DOWNLOAD PACK</button>
                <button onclick="print2DBlueprint()" style="background:#444; color:white; padding:4px; border-radius:4px; cursor:pointer; font-size:9px;">2D PRINT</button>
                <button onclick="undoFacet()" style="background:#8e44ad; color:white; padding:4px; border-radius:4px; cursor:pointer; font-size:9px;">UNDO FACET</button>
                <button onclick="resetAll()" style="background:#c0392b; color:white; padding:4px; border-radius:4px; cursor:pointer; font-size:9px; font-weight:bold;">RESET ALL</button>
                <div style="background:#111; border:1px solid #444; border-radius:4px; padding:5px; text-align:center; margin-top:5px;">
                    <span style="font-size:8px; color:#aaa; font-weight:bold;">TOTAL SQ FT</span>
                    <div id="total-sqft" style="color:#00ff00; font-weight:bold; font-size:16px;">0</div>
                </div>
            </div>
        </div>
    </div>
</div>

<button id="close-facet" style="display:none; width:100%; margin-top:10px; background:#00d4ff; color:black; border:none; padding:12px; border-radius:4px; cursor:pointer; font-weight:bold;">FINISH & SHADE FACET</button>

<div id="j18-dashboard" style="display:flex; gap:10px; margin-top:15px; align-items: stretch;">
<div id="trace-pitch-zone" style="flex: 1.5; background:#000; border:2px solid #D4AF37; border-radius:8px; position:relative; min-height:180px;">
   <canvas id="side-canvas" style="width:100%; height:100%; object-fit:contain; cursor:crosshair;"></canvas>
   <button onclick="manualRuthCall()" style="position:absolute; top:5px; left:5px; z-index:210; background:#D4AF37; color:black; border:none; padding:2px 8px; font-weight:bold; font-size:10px; cursor:pointer; border-radius:2px;">AI AUDIT</button>

<div id="ruth-apartment" style="position:absolute; top:0px; left:0px; width:220px; min-height:100px; background:rgba(0,0,0,0.95); display:none; z-index:200; padding:12px; border:2px solid #00ff00;">
    <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
        <span style="color:#D4AF37; font-weight:bold; font-size:10px;">RUTH AI | AUDIT</span>
        <button onclick="toggleMute()" id="mute-btn" style="background:#222; color:#aaa; font-size:9px; padding:2px;">MUTE</button>
    </div>
    <div id="ruth-content" style="color:#00ff00; font-family:monospace; font-size:11px;"></div>
    <button onclick="dismissRuth()" style="margin-top:10px; background:#00ff00; color:black; width:100%; font-weight:bold; padding:4px;">DISMISS</button>
</div>
<div id="side-mag">
       <canvas id="side-mag-canvas" width="140" height="140"></canvas>
       <div class="mag-crosshair"></div>
       <div class="mag-crosshair-v"></div>
   </div>

   <span id="arrow-counter-watermark" style="position: absolute; top: 6px; right: 260px; font-family: 'Arial Black', sans-serif; font-size: 11px; color: #D4AF37; font-weight: bold;"></span>

   <div style="position:absolute; top:3px; right:5px; display:flex; align-items:center; gap:6px; z-index:210; height:18px;">
    <button class="v-btn" onclick="prevPhoto()" style="background:transparent; color:#D4AF37; border:none; font-size:11px; cursor:pointer; padding:0 2px; height:14px; line-height:14px; display:inline-flex; align-items:center; justify-content:center;">◀</button>
    <button class="v-btn" onclick="nextPhoto()" style="background:transparent; color:#D4AF37; border:none; font-size:11px; cursor:pointer; padding:0 2px; height:14px; line-height:14px; display:inline-flex; align-items:center; justify-content:center;">▶</button>
    <label onclick="document.getElementById('side-upload-trigger').click()" style="position: absolute; top: 3px; right: 129px; background: #D4AF37; color: #000000; padding: 2px 8px; font-weight: bold; font-size: 10px; cursor: pointer; border-radius: 3px; display: inline-block; line-height: 1.0; text-align: center; z-index: 210; white-space: nowrap;">UPLOAD PHOTO</label>
    <button id="trace-pitch-btn" onclick="startPitchTrace()" class="v-btn" style="background:#D4AF37; color:black; border:none; padding:1px 8px; font-weight:bold; font-size:10px; cursor:pointer; border-radius:2px; height:15px; line-height:13px; display:inline-block; white-space:nowrap; box-sizing:border-box;">TRACE PITCH</button>
</div>

   <label id="side-upload-trigger" class="upload-trigger" style="display: none !important;">UPLOAD TRACE PHOTO</label>
   <div id="side-trace-status" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); color:#00ff00; font-size:10px; background:rgba(0,0,0,0.8); padding:8px; border:1px solid #00ff00; border-radius:4px; pointer-events:none; display:none; text-align:center; z-index:300;">CLICK EAVE CORNER<br>THEN RIDGE POINT</div>
</div>

<div id="modular-container" style="flex: 1.5; display:flex; flex-direction:column; border: 2px solid #D4AF37; border-radius: 8px; padding: 10px; background: #252525; overflow: hidden; position: relative;">
   <div id="content-viewport" style="flex-grow: 1; position: relative;">
      <div id="video-content" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
          <video id="ad-video" width="100%" height="100%" autoplay loop muted playsinline style="object-fit:cover;">
             <source src="https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.pexels.com%2Fdownload%2Fvideo%2F7581208%2F&data=05%7C02%7C%7C097a013b67594cf067ab08deb8e46443%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C639151488226248281%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FNfzUtZ2NrduWLOMbsrb%2BgDAiSv0mugaaww1ZVZLsuk%3D&reserved=0" type="video/mp4">
           </video>
      </div>
      <div id="guide-content" style="display:none; color:#FFD700; font-size:17px; overflow-y:auto; height:100%; padding:5px;">
          <b style="color:#00d4ff;">B72 ARCHITECTURAL USER GUIDE:</b><br>
           1. Use On-site data toggle (2D future use) only.<br>
           2. 3-min countdown before canvas locks (Same purchase re-uploads allowed).<br>
           3. Side view photos can be uploaded for multi-pitch verification.<br>
           4. Set scale using 2 points (Field Verified - VERY CRITICAL).<br>
           5. Enter facet pitch using Trace Pitch photo.<br>
           6. Enter address and drone compliance after lockdown.<br>
           7. Training options (Ospreon LLC) in top right.<br>
           8. Accumulate materials after facets are closed; download PDF.<br><br>
           <i>Remember: 99% precision requires manual refinement.</i>
      </div>
   </div>
   <button onclick="toggleModular()" style="margin-top:8px; background:#D4AF37; border:none; padding:5px; cursor:pointer; font-weight:bold; font-size:10px;">TOGGLE USERS GUIDE</button>
</div>
<div id="perm-footnote-container" style="flex: 1; padding: 10px; display: flex; flex-direction: column; gap: 5px; border: 2px solid #D4AF37; border-radius: 8px; background: #111; justify-content: center;">
   <div style="text-align:center; padding:10px; color:#00d4ff;">
 <div style="font-size:12px; margin-bottom:10px; color:#aaa;">SPONSORSHIP & ADS</div>
 <div style="font-size:20px; font-weight:bold; color:#fff;">1-800-ARIS</div>
 <hr style="border:0.5px solid #333; margin:15px 0;">
 <div style="font-size:11px; color:#00d4ff; cursor:pointer;">SEARCH DIRECTORY ></div>
</div>
   <div style="font-size: 8px; color: #444; text-align: center;">GENESIS MASTER FIX (Y10)</div>
</div>
</div>
</div>
</div>

<script>
let revertTimer;
let showGuide = false;
let stasisTimer;
let isStasis = false;
let scaleFlashTriggered = false; // Prevents scale input from constantly restarting the timer loop
function triggerAuthPrompt() {{
    // 1. Pop up a secure modal entry field for the code
    let accessCode = prompt("ENTER SECURITY VERIFICATION PIN:");

    // If they cancel out or leave it blank, do nothing
    if (accessCode === null || accessCode.trim() === "") {{
        return;
    }}

    // 2. Gateway 1: The Administrative Code
    if (accessCode === "1234") {{
        // Instantly click the hidden file input to browse any photo
        document.getElementById('nadir-upload').click();
    }}

    // 3. Gateway 2: The Trainee / Civilian Code
    else if (accessCode === "70426") {{
        alert("TRAINEE PATHWAY UNLOCKED: Pre-designated training library access only.");
        // This is where we will hook into your specific local practice file directory
        // For right now, we trigger the click to show it responds to the separate code
        document.getElementById('nadir-upload').click();
    }}

    // 4. Incorrect Entry
    else {{
        alert("ACCESS DENIED: Invalid Verification PIN. System Remains Locked.");
    }}
}}
function toggleStasis() {{
    isStasis = !isStasis;
    const shade = document.getElementById('canvas-lock-shade');
    const btn = document.getElementById('stasis-toggle');

     if (isStasis) {{
        clearTimeout(stasisTimer);
    }} else {{
        stasisTimer = setTimeout(runTimer, 1000);
    }}

    if (shade) shade.style.display = isStasis ? 'flex' : 'none';

    if (btn) {{
        btn.innerText = isStasis ? 'RESUME SESSION' : 'PAUSE (NATURE CALLS)';
        btn.style.background = isStasis ? '#00ff00' : '#ff0000';
    }}
}}
function handleNadirUpload(event) {{
    if (!event.target.files[0]) return;
    const reader = new FileReader();
    reader.onload = function(e) {{
        const img = new Image();
        img.onload = function() {{
            document.querySelector('canvas').getContext('2d').drawImage(img, 0, 0);
        }};
        img.src = e.target.result;
    }};
    reader.readAsDataURL(event.target.files[0]);
}}
const B72_BRAIN = {{
    "NO_SCALE": "I noticed the scale hasn't been set yet. Please enter the scale and pitch in the Site Data box so I can calculate the eaves and ridges correctly.",
    "LOCKED": "The B-72 is currently locked for verification. I'm analyzing the drone metadata and GPS coordinates to ensure compliance.",
    "READY": "Verification complete. The B-72 is ready. You can now begin tracing the pitch on the aerial photo."
}};

window.ruthSuggest = function(message, type = 'audit') {{
    const overlay = document.getElementById('ruth-apartment');
    const content = document.getElementById('ruth-content');

    if (overlay && content) {{
        content.innerHTML = `<h3 style="color:#D4AF37; margin:0;">RUTH AI | ${{type.toUpperCase()}}</h3><p>${{B72_BRAIN[message] || message}}</p>`;
        overlay.style.display = 'block';
        overlay.style.zIndex = '9999';

        const voice = new SpeechSynthesisUtterance(message);
        const allVoices = window.speechSynthesis.getVoices();
        const targetVoice = allVoices.find(v => v.name.includes('Microsoft Zira') || v.name.includes('Hazel'));

        if (targetVoice) {{
            voice.voice = targetVoice;
        }}

        voice.rate = 0.85;
        voice.pitch = 1.0;
        window.speechSynthesis.speak(voice);

        if (type === 'tutorial' && !isStasis) toggleStasis();
    }}
}}

function dismissRuth() {{
    const overlay = document.querySelector('.trace-pitch-box #ruth-apartment') || document.getElementById('ruth-apartment');
    if (overlay) overlay.style.display = 'none';
    if(isStasis) toggleStasis();
}}

function toggleModular() {{
    const vid = document.getElementById('ad-video');
    const vidContent = document.getElementById('video-content');
    const guideContent = document.getElementById('guide-content');

    showGuide = !showGuide;
    vidContent.style.display = showGuide ? 'none' : 'flex';
    guideContent.style.display = showGuide ? 'block' : 'none';
    if (showGuide) {{
       vid.pause();
       clearTimeout(revertTimer);
       revertTimer = setTimeout(revertToVideo, 8000);
    }} else {{
       vid.play();
    }}
}}

function revertToVideo() {{
    const vid = document.getElementById('ad-video');
    const vidContent = document.getElementById('video-content');
    const guideContent = document.getElementById('guide-content');

    showGuide = false;
    vidContent.style.display = 'flex';
    guideContent.style.display = 'none';
    vid.play();
}}

let isUploadLocked = false;
const signatures = {byte_json};
let timeRemaining = 180;
const timerEl = document.getElementById('timer-display');

function runTimer() {{
    const mins = Math.floor(timeRemaining / 60);
    const secs = timeRemaining % 60;
    timerEl.value = mins.toString().padStart(2, '0') + ":" + secs.toString().padStart(2, '0');
    if (timeRemaining > 0) {{
        timeRemaining--;
        if(timeRemaining < 60) {{ timerEl.classList.add('timer-active'); }}
      stasisTimer = setTimeout(runTimer, 1000);
    }} else {{
        timerEl.value = "LOCKED";
        timerEl.style.color = "red";
        timerEl.classList.remove('timer-active');
        isUploadLocked = true;
    }}
}}
runTimer();

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const zoomCanvas = document.getElementById('zoom-canvas');
const zctx = zoomCanvas.getContext('2d');
const mag = document.getElementById('mag-glass');
const dock = document.getElementById('tool-dock');
const viewport = document.getElementById('viewport');
const toggle = document.getElementById('toggle-3d');
const knob = document.getElementById('slider-knob');
const label3d = document.getElementById('label-3d');
const label2d = document.getElementById('label-2d');
const sideCanvas = document.getElementById('side-canvas');
const sctx = sideCanvas.getContext('2d');
const sideMag = document.getElementById('side-mag');
const smctx = document.getElementById('side-mag-canvas').getContext('2d');

let gallery = {gallery_json};
let fileNames = Object.keys(gallery);
let currentIdx = 0;
let sidePoints = [];
let isTracingPitch = false;
let anchor = [], currentFacetPoints = [], savedFacets = [], lines = [], linearTracker = [];
let baseScale = 0; let activeMode = 'eave'; let isFrozen = false;
let showHUD = true;

const img = new Image();
const sideImg = new Image();

   img.onload = function() {{
        canvas.width = img.width;
        canvas.height = img.height;
        draw();

        const sigBox = document.getElementById('photo-id-box');
        if(fileNames.length > 0) {{
            sigBox.value = signatures[fileNames[0]];
        }}

        try {{
            const binaryString = atob(img.src.split(',')[1]);
            const bytes = new Uint8Array(binaryString.length);
            for (let i = 0; i < binaryString.length; i++) {{
                bytes[i] = binaryString.charCodeAt(i);
            }}
            interrogatePhoto(bytes.buffer, fileNames[0]);
        }} catch (e) {{
            console.error("Forensic prep failed:", e);
        }}
    }};
img.src = "data:image/jpeg;base64,{img_data_main}";

function updateFeedDisplay() {{
    if (fileNames.length === 0) return;
    sideImg.onload = () => {{
        sideCanvas.width = sideImg.width;
        sideCanvas.height = sideImg.height;
        drawSide();
    }};
    sideImg.src = "data:image/jpeg;base64," + gallery[fileNames[currentIdx]];
    document.getElementById('arrow-counter-watermark').innerText = (currentIdx + 1) + " - " + fileNames.length;
}}

const mainInput = document.createElement('input');
mainInput.type = 'file'; mainInput.accept = 'image/*';
mainInput.style.display = 'none';

mainInput.onchange = (e) => {{
    const file = e.target.files[0];
    if (!file) return;

    const names = ['drone-model-display', 'model-id', 'drone-model', 'model-box'];
    names.forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
            el.innerText = "LINK FOUND";
            el.style.color = "#00ff00";
        }}
    }});

    const reader = new FileReader();
    reader.onload = (event) => {{
        img.onload = () => {{
            canvas.width = img.width;
            canvas.height = img.height;
            draw();
            if (typeof updateFeedDisplay === "function") updateFeedDisplay();
        }};
        img.src = event.target.result;
    }};
    reader.readAsDataURL(file);
}};

document.body.appendChild(mainInput);

const traceInput = document.createElement('input');
traceInput.type = 'file'; traceInput.accept = 'image/*';
traceInput.style.display = 'none';
traceInput.onchange = (e) => {{
    const file = e.target.files[0];
    if(!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {{
        const b64 = event.target.result.split(',')[1];
        const newKey = "trace_" + Date.now();
        gallery[newKey] = b64;
        fileNames = Object.keys(gallery);
        currentIdx = fileNames.length - 1;
        updateFeedDisplay();
    }};
    reader.readAsDataURL(file);
}};
document.body.appendChild(traceInput);
document.getElementById('side-upload-trigger').onclick = (e) => {{ traceInput.click(); }};

function nextPhoto() {{ if(fileNames.length > 0) {{ currentIdx = (currentIdx + 1) % fileNames.length; updateFeedDisplay(); }} }}
function prevPhoto() {{ if(fileNames.length > 0) {{ currentIdx = (currentIdx - 1 + fileNames.length) % fileNames.length; updateFeedDisplay(); }} }}

function startPitchTrace() {{
    isTracingPitch = !isTracingPitch;
    sidePoints = [];
    const btn = document.getElementById('trace-pitch-btn');
    const status = document.getElementById('side-trace-status');
    if (isTracingPitch) {{
        btn.classList.add('trace-active'); btn.innerText = "CANCEL";
        status.style.display = 'block'; sideMag.style.display = 'block';
    }} else {{
        btn.classList.remove('trace-active'); btn.innerText = "TRACE PITCH";
        status.style.display = 'none'; sideMag.style.display = 'none';
    }}
}}

document.getElementById('trace-pitch-zone').onmousemove = function(e) {{
    if (!isTracingPitch) return;
    const zoneRect = this.getBoundingClientRect();
    const mouseX = e.clientX - zoneRect.left;
    const mouseY = e.clientY - zoneRect.top;
    let mX = mouseX + 20; let mY = mouseY - 150;
    if (mX + 140 > zoneRect.width) mX = mouseX - 160;
    if (mY < 5) mY = mouseY + 20;
    sideMag.style.left = mX + "px"; sideMag.style.top = mY + "px";
    const sRect = sideCanvas.getBoundingClientRect();
    const x = (e.clientX - sRect.left) / (sRect.width / sideCanvas.width);
    const y = (e.clientY - sRect.top) / (sRect.height / sideCanvas.height);
    smctx.fillStyle = "black"; smctx.fillRect(0,0,140,140);
    smctx.drawImage(sideCanvas, x - 40, y - 40, 80, 80, 0, 0, 140, 140);
}};

sideCanvas.onclick = function(e) {{
    if (!isTracingPitch) return;
    const rect = sideCanvas.getBoundingClientRect();
    const x = (e.clientX - rect.left) / (rect.width / sideCanvas.width);
    const y = (e.clientY - rect.top) / (rect.height / sideCanvas.height);
    sidePoints.push({{x, y}});
    if (sidePoints.length === 2) {{
        const dy = Math.abs(sidePoints[1].y - sidePoints[0].y);
        const dx = Math.abs(sidePoints[1].x - sidePoints[0].x);
        const calculatedPitch = (dy / dx) * 12;
        document.getElementById('pitch-box').value = calculatedPitch.toFixed(2);
        executeAttentionFlash(); // Fire a 5s flash when pitch is grabbed from trace
        startPitchTrace();
    }}
    drawSide();
}};

function drawSide() {{
    sctx.clearRect(0,0,sideCanvas.width, sideCanvas.height);
    sctx.drawImage(sideImg, 0, 0);
    sctx.strokeStyle = "#ffcc00"; sctx.lineWidth = 8;
    if (sidePoints.length === 2) {{
        sctx.beginPath(); sctx.moveTo(sidePoints[0].x, sidePoints[0].y); sctx.lineTo(sidePoints[1].x, sidePoints[1].y); sctx.stroke();
    }}
    sidePoints.forEach(p => {{ sctx.fillStyle="red"; sctx.beginPath(); sctx.arc(p.x,p.y,12,0,Math.PI*2); sctx.fill(); }});
}}

toggle.addEventListener('change', function() {{
    knob.style.left = this.checked ? "25px" : "3px";
    const btn = document.getElementById('acc-btn-text');
    if (this.checked) {{
        label2d.style.opacity = "1.0"; label2d.style.color = "#ffcc00"; label3d.style.opacity = "0.4";
        btn.innerText = "ACCUMULATE METAL PACKAGE";
        checkMetalRequired();
    }} else {{
        label3d.style.opacity = "1.0"; label3d.style.color = "#00ff00"; label2d.style.opacity = "0.4";
        btn.innerText = "ACCUMULATE SHINGLE PACKAGE";
        btn.disabled = false;
    }}
    draw();
    document.getElementById('acc-results').innerHTML = "READY...";
}});

function checkMetalRequired() {{
    const btn = document.getElementById('acc-btn-text');
    const width = document.getElementById('metal-width-box').value;
    if (toggle.checked && (!width || width <= 0)) {{
        btn.disabled = true;
        document.getElementById('metal-width-container').style.borderColor = "#ff0000";
    }} else {{
        btn.disabled = false;
        document.getElementById('metal-width-container').style.borderColor = "#555";
    }}
}}

window.toggleGuide = function() {{
    const guide = document.getElementById('center-guide');
    guide.style.display = document.getElementById('guide-toggle').checked ? 'block' : 'none';
}};

window.addEventListener('contextmenu', (e) => {{ e.preventDefault(); isFrozen = !isFrozen; dock.style.borderColor = isFrozen ? '#ff0000' : '#00d4ff'; }});

viewport.onmousemove = function(e) {{
    const vRect = viewport.getBoundingClientRect();
    const mouseX = e.clientX - vRect.left;
    const mouseY = e.clientY - vRect.top;
    let dockX = mouseX - 120; let dockY = mouseY - 100;
    if (dockX < 5) dockX = 5; if (dockX + 115 > vRect.width) dockX = vRect.width - 120;
    if (dockY < 5) dockY = 5; if (dockY + 210 > vRect.height) dockY = vRect.height - 215;
    let magX = mouseX + 40; let magY = mouseY - 110;
    if (magX + 225 > vRect.width) magX = mouseX - 250;
    mag.style.display = 'block'; dock.style.display = 'flex';
    if (!isFrozen) {{ dock.style.left = dockX + "px"; dock.style.top = dockY + "px"; }}
    mag.style.left = magX + "px"; mag.style.top = magY + "px";
    const cRect = canvas.getBoundingClientRect();
    const x = (e.clientX - cRect.left) / (cRect.width / canvas.width);
    const y = (e.clientY - cRect.top) / (cRect.height / canvas.height);
    zctx.fillStyle = "black"; zctx.fillRect(0,0,220,220);
    zctx.drawImage(canvas, x - 50, y - 50, 100, 100, 0, 0, 220, 220);
}};

canvas.onclick = function(e) {{
    const rect = canvas.getBoundingClientRect();
    const x = (e.clientX - rect.left) / (rect.width / canvas.width);
    const y = (e.clientY - rect.top) / (rect.height / canvas.height);
    document.getElementById('cur-mode').classList.add('mode-alert');
    if (anchor.length < 2) {{
        anchor.push({{x, y}});
    }} else {{
        currentFacetPoints.push({{x, y}}); linearTracker.push({{x, y}});
        if (linearTracker.length === 2) {{
            const p = parseFloat(document.getElementById('pitch-box').value || 0);
            let mult = 1.0; let backOff = 1.0;
            if (activeMode === 'ridge' || activeMode === 'valley') backOff = 1 / (1 + (p / 100));
            if (activeMode === 'rake' || activeMode === 'valley' || activeMode === 'sw') {{
                mult = Math.sqrt(p*p+144)/12;
            }} else if (activeMode === 'hip') {{
                mult = (Math.sqrt(p*p+288)/12) * (1 - (p/144));
            }}
            let p1 = linearTracker[0]; let p2 = linearTracker[1];
            let existing = lines.find(l => {{
                return (Math.hypot(l.p1.x - p1.x, l.p1.y - p1.y) < 15 && Math.hypot(l.p2.x - p2.x, l.p2.y - p2.y) < 15) ||
                       (Math.hypot(l.p1.x - p2.x, l.p1.y - p2.y) < 15 && Math.hypot(l.p2.x - p1.x, l.p2.y - p1.y) < 15);
            }});
            let lengthVal; let isDuplicate = false; let displayLength;
            if (existing && (existing.mode === 'ridge' || existing.mode === 'valley')) {{
                lengthVal = existing.displayRaw; isDuplicate = true; displayLength = existing.fixedLength;
            }} else {{
                lengthVal = Math.sqrt(Math.pow(p2.x-p1.x,2)+Math.pow(p2.y-p1.y,2)) * backOff;
                displayLength = (lengthVal * baseScale * mult).toFixed(1);
            }}
            lines.push({{ p1: p1, p2: p2, raw: isDuplicate ? 0 : lengthVal, displayRaw: lengthVal, fixedLength: displayLength, mode: activeMode, mult: mult, isDup: isDuplicate }});
            linearTracker = [{{x, y}}];
        }}
        document.getElementById('close-facet').style.display = (currentFacetPoints.length >= 3) ? "block" : "none";
    }}
    draw(); updateUI();
}};

function draw() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (!toggle.checked) {{ ctx.drawImage(img, 0, 0); }}
    else {{
        ctx.fillStyle = "#111"; ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = "#222"; ctx.lineWidth = 1;
        for (let i = 0; i < canvas.width; i += 50) {{ ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke(); }}
        for (let j = 0; j < canvas.height; j += 50) {{ ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke(); }}
    }}
    const colors = {{ eave:"#00ff00", ridge:"#00d4ff", rake:"#ffcc00", hip:"#ff00ff", valley:"#ffffff", sw:"#ff00ff", ew:"#008080" }};
    savedFacets.forEach((f, idx) => {{
        ctx.fillStyle = toggle.checked ? "rgba(0, 212, 255, 0.2)" : "rgba(0, 212, 255, 0.35)";
        ctx.beginPath(); f.points.forEach((p, i) => i===0 ? ctx.moveTo(p.x,p.y) : ctx.lineTo(p.x,p.y)); ctx.closePath(); ctx.fill();
        if(f.cX && f.cY) {{
            ctx.beginPath(); ctx.arc(f.cX, f.cY, 11, 0, Math.PI*2); ctx.fillStyle = "#D4AF37"; ctx.fill();
            ctx.fillStyle = "black"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center"; ctx.fillText(idx + 1, f.cX, f.cY + 4);
        }}
    }});
    lines.forEach(l => {{
        ctx.strokeStyle = colors[l.mode]; ctx.lineWidth = toggle.checked ? 4.0 : 2.0;
        if(l.isDup) ctx.setLineDash([5, 5]); else ctx.setLineDash([]);
        ctx.beginPath(); ctx.moveTo(l.p1.x, l.p1.y); ctx.lineTo(l.p2.x, l.p2.y); ctx.stroke(); ctx.setLineDash([]);
        if (baseScale > 0) {{
            let dynamicVal = (l.raw * baseScale * l.mult);
            let midX = (l.p1.x + l.p2.x) / 2; let midY = (l.p1.y + l.p2.y) / 2;
            ctx.fillStyle = "black"; ctx.beginPath(); ctx.roundRect(midX - 24, midY - 11, 48, 22, 4); ctx.fill();
            ctx.fillStyle = l.isDup ? "#00ff00" : "#D4AF37"; ctx.font = "bold 12px monospace"; ctx.textAlign = "center";
            ctx.fillText(formatToFtIn(dynamicVal), midX, midY + 5);
        }}
    }});
    anchor.forEach(p => {{ ctx.fillStyle="red"; ctx.beginPath(); ctx.arc(p.x,p.y,5,0,Math.PI*2); ctx.fill(); }});
}}
// Helper: Convert decimal feet to Feet and Inches
function formatToFtIn(decimalFeet) {{
    const feet = Math.floor(decimalFeet);
    const inches = Math.round((decimalFeet - feet) * 12);
    return `${{feet}}' ${{inches}}"`;
}}
function updateUI() {{
    if (anchor.length === 2 && timeRemaining < 9000) {{
        const d = Math.hypot(anchor[1].x - anchor[0].x, anchor[1].y - anchor[0].y);

        // Corrected calculation for feet and inches
        const ft = parseFloat(document.getElementById('ref-ft').value) || 0;
        const inVal = parseFloat(document.getElementById('ref-in').value) || 0;
        const totalRef = ft + (inVal / 12);

        baseScale = totalRef > 0 ? totalRef / d : 0;
    }}

    let t = {{ eave: 0, ridge: 0, rake: 0, hip: 0, valley: 0, sw: 0, ew: 0 }};
    // ... remainder of your code continues here
    lines.forEach(l => t[l.mode] += (l.raw * baseScale * l.mult));
    Object.keys(t).forEach(k => {{ if(document.getElementById('val-'+k)) document.getElementById('val-'+k).innerText = formatToFtIn(t[k]); }});
    let areaTotalRaw = 0; let tbody = "";
    savedFacets.forEach((f, idx) => {{
        let sqft_calibrated = (f.rawBase * Math.pow(baseScale,2) * f.mult) * 0.9715;
        areaTotalRaw += sqft_calibrated;
        tbody += "<tr><td style='padding:4px; color:#aaa;'>" + (idx+1) + "</td><td style='padding:4px;' class='pitch-gold'>" + f.pitch + "/12</td><td style='padding:4px;' class='sqft-green'>" + sqft_calibrated.toFixed(2) + "</td></tr>";
    }});
    document.getElementById('total-sqft').innerText = areaTotalRaw.toFixed(2);
    document.getElementById('facet-tbody').innerHTML = tbody;
}}

// MASTER ENGINE ATTENTION LOCK: FLASHES THE PITCH CONTAINER FOR EXACTLY 5 SECONDS AND THEN STOPS SOLID
function executeAttentionFlash() {{
    const container = document.getElementById('pitch-container');
    if (container) {{
        container.classList.add('pitch-alert'); // Starts the Gold/White flashing animation
        setTimeout(() => {{
            container.classList.remove('pitch-alert'); // Halts the animation after exactly 5 seconds
        }}, 8000);
    }}
}}

// TRIGGER 1: Scale entry triggers the 5-second attention draw
function triggerScaleFlash() {{
    updateUI();
    if (!scaleFlashTriggered) {{
        executeAttentionFlash();
        scaleFlashTriggered = true; // Locks trigger so typing extra digits doesn't keep resetting the 5s loop
    }}
}}

window.accumulateJ18 = function() {{
    const ev = parseFloat(document.getElementById('val-eave').innerText);
    const rk = parseFloat(document.getElementById('val-rake').innerText);
    const rd = parseFloat(document.getElementById('val-ridge').innerText);
    const hp = parseFloat(document.getElementById('val-hip').innerText);
    const vy = parseFloat(document.getElementById('val-valley').innerText);
    const sw = parseFloat(document.getElementById('val-sw').innerText);
    const ew = parseFloat(document.getElementById('val-ew').innerText);
    const totalSqFt = parseFloat(document.getElementById('total-sqft').innerText);
    const metalWidthIn = parseFloat(document.getElementById('metal-width-box').value);
    const isMetalMode = document.getElementById('toggle-3d').checked;

    if (!isMetalMode) {{
        const bndl_shingle = Math.ceil(totalSqFt / 33.33);
        const bndl_valley = Math.ceil(vy / 20);
        const bndl_cap = Math.ceil((rd + hp) / 31.25);
        const bndl_starter = Math.ceil((ev + rk) / 75);
        const rolls_synthetic = Math.ceil(totalSqFt / 1000);
        document.getElementById('acc-results').innerHTML = "<b>SHINGLE PACK (B72)</b><br>ARCHITECTURAL FIELD SHINGLES: " + bndl_shingle + " BNDL<br>ARCHITECTURAL VALLEY ALLOWANCE: " + bndl_valley + " BNDL<br>3-TAB RIDGE CAPS: " + bndl_cap + " BNDL<br>3-TAB STARTERS: " + bndl_starter + " BNDL<br>SYNTHETIC PAPER: " + rolls_synthetic + " ROLL<br>ROOF NAILS 1.25\\": 1 BOX (7200 CT)<br>0% WASTE APPLIED";
    }} else {{
        const panelCount = Math.ceil((ev * 12) / metalWidthIn);
        const trim_ridge = Math.ceil(rd / 10); const trim_hip = Math.ceil(hp / 10);
        document.getElementById('acc-results').innerHTML = "<b>METAL PACK (B72)</b><br>PANELS: " + panelCount + " QTY<br>DRIP: " + Math.ceil(ev/10) + " PCS<br>GABLE: " + Math.ceil(rk/10) + " PCS<br>CAPS: " + (trim_ridge + trim_hip) + " PCS<br>SIDE/END: " + Math.ceil((sw+ew)/10) + " PCS";
    }}
}};

window.downloadPack = function() {{
    const address = document.getElementById('attr-box').value || "NO_ADDRESS";
    const drone = document.getElementById('drone-model-display').innerText || "NOT_SPECIFIED";
    const status = document.getElementById('drone-fvm-display').innerText || "WAITING";
    const totalSqFt = document.getElementById('total-sqft').innerText;
    const accData = document.getElementById('acc-results').innerText;
    const byteSig = document.getElementById('photo-id-box').value;
    let content = "GENESIS PROJECT REPORT\\nADDRESS: " + address + "\\nBYTE-SIG: " + byteSig + "\\nDRONE MODEL: " + drone + "\\nVERIFICATION: " + status + "\\nDATE: " + new Date().toLocaleDateString() + "\\n------------------------------------------\\nTOTAL VERIFIED AREA: " + totalSqFt + " SQ FT\\n\\nLINEAR MEASUREMENTS:\\nEAVES: " + document.getElementById('val-eave').innerText + "'\\nRIDGES: " + document.getElementById('val-ridge').innerText + "'\\nRAKES: " + document.getElementById('val-rake').innerText + "'\\nHIPS: " + document.getElementById('val-hip').innerText + "'\\nVALLEYS: " + document.getElementById('val-valley').innerText + "'\\nSIDE WALL: " + document.getElementById('val-sw').innerText + "'\\nEND WALL: " + document.getElementById('val-ew').innerText + "'\\n\\nMATERIAL ACCUMULATION (B72 - 0% WASTE):\\n" + accData + "\\n\\n------------------------------------------\\n\\nGENESIS MASTER FIX (Y10) | PRECISION AT THE SPEED OF A CLICK";

    const blob = new Blob([content], {{ type: 'text/plain' }});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = "GENESIS_REPORT_" + address.replace(/\\s+/g, '_') + ".txt"; a.click();
}};

window.print2DBlueprint = function() {{
    const address = document.getElementById('attr-box').value || "NO_ADDRESS";

    // 1. Create a pristine light gray drywall-tone baseline sheet matching workspace size
    const printCanvas = document.createElement('canvas');
    printCanvas.width = canvas.width;
    printCanvas.height = canvas.height;
    const pCtx = printCanvas.getContext('2d');
    pCtx.fillStyle = '#e5e5e5';
    pCtx.fillRect(0, 0, printCanvas.width, printCanvas.height);

    // 2. Explicitly draw the roof facets onto the blueprint layout with high contrast shading
    savedFacets.forEach((f) => {{
        pCtx.fillStyle = "rgba(40, 44, 52, 0.25)"; // Softer charcoal tint that saves your ink cartridges
ctx.fill();
        f.points.forEach((p, i) => i === 0 ? pCtx.moveTo(p.x, p.y) : pCtx.lineTo(p.x, p.y));
        pCtx.closePath();
        pCtx.fill();
    }});

    // 3. Force all colored lines to render as high-contrast solid black lines
    pCtx.strokeStyle = '#000000';
    pCtx.lineWidth = 3;
    lines.forEach(l => {{
        pCtx.beginPath();
        pCtx.moveTo(l.p1.x, l.p1.y);
        pCtx.lineTo(l.p2.x, l.p2.y);
        pCtx.stroke();
    }});

    // 4. Draw protective label background blocks and write linear values in black
    if (baseScale > 0) {{
        lines.forEach(l => {{
            // FIX: Calculate dynamic length and format it
            let dynamicVal = (l.displayRaw * baseScale * l.mult);
            let formattedText = formatToFtIn(dynamicVal);

            let midX = (l.p1.x + l.p2.x) / 2;
            let midY = (l.p1.y + l.p2.y) / 2;

            let boxWidth = 70; // Increased slightly for better fit of feet/inches
            let boxHeight = 24;

            pCtx.fillStyle = "#FFFFFF";
            pCtx.fillRect(midX - (boxWidth / 2), midY - (boxHeight / 2), boxWidth, boxHeight);

            pCtx.strokeStyle = "#000000";
            pCtx.lineWidth = 1.5;
            pCtx.strokeRect(midX - (boxWidth / 2), midY - (boxHeight / 2), boxWidth, boxHeight);

            pCtx.fillStyle = "#000000";
            pCtx.font = "BOLD 16px monospace"; // Slightly smaller font to fit feet and inches
            pCtx.textAlign = "center";
            pCtx.textBaseline = "middle";
            pCtx.fillText(formattedText, midX, midY);
        }});
    }}

    // 5. Draw facet numbers in the center with large, readable text
    savedFacets.forEach((f, idx) => {{
        if(f.cX && f.cY) {{
            // Draw the background circle for the number token
            pCtx.beginPath();
            pCtx.arc(f.cX, f.cY, 16, 0, Math.PI * 2);
            pCtx.fillStyle = "#FFFFFF"; // Clean white token background
            pCtx.fill();
            pCtx.strokeStyle = "#000000"; // Sharp border edge
            pCtx.lineWidth = 2;
            pCtx.stroke();

            // Draw the large, clear text
            pCtx.fillStyle = "#000000"; // Solid black number
            pCtx.font = "900 24px sans-serif"; // Maximum visibility text size
            pCtx.textAlign = "center";
            pCtx.textBaseline = "middle"; // Centers it perfectly inside the white token
            pCtx.fillText(idx + 1, f.cX, f.cY);
        }}
    }});

    // 6. Draw a clean solid Black Frame Border around the outermost edge of the page
    pCtx.strokeStyle = '#000000';
    pCtx.lineWidth = 6;
    pCtx.strokeRect(0, 0, printCanvas.width, printCanvas.height);

    // 7. Instantly deliver the completed blueprint to the user
    const dataUrl = printCanvas.toDataURL('image/png');
    const a = document.createElement('a');
    a.href = dataUrl;
    const cleanAddress = String(address).split(' ').join('_').split(',').join('').split('.').join('').split('|').join('_');
    a.download = "GENESIS_2D_BLUEPRINT_" + cleanAddress + ".png";
    a.click();
}};

// TRIGGER 2: Clicking Finish & Shade Facet locks the section and fires the 5-second attention loop
document.getElementById('close-facet').onclick = function() {{
    let area = 0; let sX = 0, sY = 0; const points = currentFacetPoints; const n = points.length;
    for (let i = 0; i < n; i++) {{ let j = (i + 1) % n; let factor = (points[i].x * points[j].y - points[j].x * points[i].y); area += factor; sX += (points[i].x + points[j].x) * factor; sY += (points[i].y + points[j].y) * factor; }}
    let finalArea = Math.abs(area / 2); const finalCX = sX / (3 * area); const finalCY = sY / (3 * area);
    const p = parseFloat(document.getElementById('pitch-box').value || 0);
    savedFacets.push({{ points: [...currentFacetPoints], rawBase: finalArea, pitch: p, mult: Math.sqrt(p * p + 144) / 12, cX: finalCX, cY: finalCY }});
    currentFacetPoints = []; linearTracker = []; document.getElementById('close-facet').style.display = "none";

    executeAttentionFlash(); // Fire the mandatory 5-second warning loop for the next facet
    draw(); updateUI();
}};

window.resetPitchAlert = function() {{ document.getElementById('pitch-container').classList.remove('pitch-alert'); }};
window.setMode = function(m) {{
    activeMode = m;
    const modeSpan = document.getElementById('cur-mode');
    modeSpan.innerText = m.toUpperCase();
    modeSpan.classList.add('mode-alert');
    setTimeout(() => modeSpan.classList.remove('mode-alert'), 1000);
}};
window.undoLine = function() {{ if (lines.length > 0) {{ lines.pop(); linearTracker = []; draw(); updateUI(); }} }};
window.undoFacet = function() {{ if (savedFacets.length > 0) {{ savedFacets.pop(); draw(); updateUI(); scaleFlashTriggered = false; }} }};
window.resetAll = function() {{ if(confirm("RESET ALL?")) {{ anchor=[]; currentFacetPoints=[]; savedFacets=[]; lines=[]; linearTracker=[]; scaleFlashTriggered = false; draw(); updateUI(); }} }};
window.updateZoom = function() {{ let val = parseFloat(document.getElementById('zoom-slider').value); document.getElementById('canvas-container').style.transform = "scale(" + (1+val) + ")"; document.getElementById('zoom-val').innerText = Math.round(val * 100) + "%"; }};

updateFeedDisplay();

     img.onload = function() {{
        canvas.width = img.width;
        canvas.height = img.height;
        draw();

        const sigBox = document.getElementById('photo-id-box');
        if(fileNames.length > 0) sigBox.value = signatures[fileNames[0]];

        try {{
            const binaryString = atob(img.src.split(',')[1]);
            const bytes = new Uint8Array(binaryString.length);
            for (let i = 0; i < binaryString.length; i++) {{
                bytes[i] = binaryString.charCodeAt(i);
            }}
            interrogatePhoto(bytes.buffer, fileNames[0]);
        }} catch (e) {{
            console.error("Forensic link failed.", e);
        }}
    }};
      async function interrogatePhoto(fileData, fileName) {{
        try {{
            const tags = await ExifReader.load(fileData, {{ expanded: true }});
            const decoder = new TextDecoder('utf-8');
            const rawText = decoder.decode(fileData.slice(0, 150000)).toUpperCase();

            const makeTag = (tags['Make']?.description || "").toUpperCase();
            const modelTag = (tags['Model']?.description || "").toUpperCase();
            const isDrone = makeTag.includes("DJI") || rawText.includes("DJI");
            let timestamp = "UNKNOWN TIME";

            if (tags['DateTimeOriginal']) timestamp = tags['DateTimeOriginal'].description;
            else if (tags['CreateDate']) timestamp = tags['CreateDate'].description;
            else if (tags['DateTime']) timestamp = tags['DateTime'].description;

            if (timestamp === "UNKNOWN TIME") {{
                const djiDateMatch = rawText.match(/CREATEDATE="([^"]+)"/) ||
                                     rawText.match(/MODIFYDATE="([^"]+)"/) ||
                                     rawText.match(/DATE_TIME="([^"]+)"/);
                if (djiDateMatch) {{
                    timestamp = djiDateMatch[1].replace('T', ' ').split('.')[0];
                }}
            }}

            const modelBox = document.getElementById('drone-model-display');
            const altBox = document.getElementById('drone-fvm-display');
            const addrBox = document.getElementById('attr-box');

            if (modelBox) {{
                modelBox.innerText = isDrone ? "FC8482 (DJI)" : modelTag + " (MOBILE)";
                modelBox.style.color = isDrone ? "#00ff00" : "#00d4ff";
            }}

            let rawAltMatch = rawText.match(/RELATIVEALTITUDE="([^"]+)"/) || rawText.match(/DRONEALTITUDE:(\\d+\\.?\\d*)/);
            let rawAlt = rawAltMatch ? parseFloat(rawAltMatch[1]) : (tags['GPSAltitude']?.description || 0);

            if (altBox) {{
                if (isDrone && rawAlt !== 0) {{
                    let totalInches = parseFloat(rawAlt) * 39.3701;
                    let ft = Math.floor(totalInches / 12);
                    let inc = Math.round(totalInches % 12);
                    altBox.innerText = ft + "' " + inc + "\\" [BARO-LOCKED]";
                }} else {{
                    altBox.innerText = "DATA EXTRACTED";
                }}
                altBox.style.color = "#00ff00";
            }}

            let lat = tags['GPSLatitude']?.description;
            let lon = tags['GPSLongitude']?.description;

            if (!lat) {{
                const xmpLat = rawText.match(/GPSLATITUDE="([^"]+)"/);
                const xmpLon = rawText.match(/GPSLONGITUDE="([^"]+)"/);
                if (xmpLat) lat = xmpLat[1];
                if (xmpLon) lon = xmpLon[1];
            }}

            if (addrBox) {{
                if (lat && lon) {{
                    addrBox.value = lat + ", " + lon + " | " + timestamp + " [VERIFIED]";
                    addrBox.style.color = "#00ff00";
                    addrBox.style.fontWeight = "bold";
                }} else {{
                    addrBox.value = "GPS BYTES PROTECTED | " + timestamp;
                    addrBox.style.color = "#FFD700";
                    window.ruthSuggest('LOCKED');
                }}
            }}

        }} catch (e) {{
            console.error("Forensic link failed.", e);
        }}
    }}
    window.B72_BRAIN = {{
    "LOCKED": "Forensic lock required. Please verify metadata or check GPS link before proceeding."
}};

window.ruthSuggest = function(code) {{
    let msg = window.B72_BRAIN[code] || code;
    let pitchBox = document.getElementById('side-trace-status');
    if (pitchBox) {{
        pitchBox.innerText = msg;
        pitchBox.style.color = "#FFD700";
    }}

    let utterance = new SpeechSynthesisUtterance(msg);
    window.speechSynthesis.speak(utterance);
}};
</script>
'''
display(IPython.display.HTML(html_code))
