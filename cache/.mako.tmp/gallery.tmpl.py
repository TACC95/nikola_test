# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1784466318.812958
_enable_loop = True
_template_filename = 'templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_head', 'content', 'extra_js']


import json 

from urllib.parse import quote 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('post_helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'post_helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        photo_array = context.get('photo_array', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        folders = context.get('folders', UNDEFINED)
        title = context.get('title', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        post = context.get('post', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        lang = context.get('lang', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photo_array = context.get('photo_array', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        post = context.get('post', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n')
        if photo_array and post and post.meta('music'):
            __M_writer('    /* 单个相册页底部音乐播放器 */\n    body.has-gallery-player {\n        padding-bottom: 80px;\n    }\n    #gallery-player {\n        position: fixed;\n        bottom: 0;\n        left: 0;\n        right: 0;\n        height: 70px;\n        background: rgba(30, 30, 35, 0.96);\n        color: #fff;\n        display: flex;\n        align-items: center;\n        justify-content: space-between;\n        padding: 0 24px;\n        z-index: 1000;\n        box-shadow: 0 -2px 12px rgba(0,0,0,0.35);\n        font-size: 14px;\n    }\n    .player-info {\n        display: flex;\n        align-items: center;\n        gap: 12px;\n        width: 220px;\n        flex-shrink: 0;\n    }\n    .player-cover {\n        width: 48px;\n        height: 48px;\n        background: linear-gradient(135deg, #444, #222);\n        border-radius: 4px;\n        display: flex;\n        align-items: center;\n        justify-content: center;\n        font-size: 24px;\n    }\n    .player-title {\n        font-size: 14px;\n        color: #fff;\n        margin-bottom: 4px;\n    }\n    .player-artist {\n        font-size: 12px;\n        color: #999;\n    }\n    .player-controls {\n        display: flex;\n        align-items: center;\n        gap: 16px;\n        flex-shrink: 0;\n    }\n    .player-btn {\n        background: none;\n        border: none;\n        color: #ddd;\n        font-size: 20px;\n        cursor: pointer;\n        padding: 4px 8px;\n        transition: color 0.2s;\n    }\n    .player-btn:hover {\n        color: #fff;\n    }\n    .player-play {\n        font-size: 28px;\n    }\n    .player-progress {\n        display: flex;\n        align-items: center;\n        gap: 10px;\n        flex: 1;\n        max-width: 500px;\n        margin: 0 24px;\n    }\n    .player-progress input[type="range"] {\n        flex: 1;\n        height: 4px;\n        -webkit-appearance: none;\n        background: #555;\n        border-radius: 2px;\n        outline: none;\n    }\n    .player-progress input[type="range"]::-webkit-slider-thumb {\n        -webkit-appearance: none;\n        width: 12px;\n        height: 12px;\n        background: #fff;\n        border-radius: 50%;\n        cursor: pointer;\n    }\n    .player-time {\n        font-size: 12px;\n        color: #aaa;\n        min-width: 38px;\n        text-align: center;\n    }\n    .player-volume {\n        display: flex;\n        align-items: center;\n        gap: 8px;\n        width: 140px;\n        flex-shrink: 0;\n    }\n    .player-volume input[type="range"] {\n        flex: 1;\n        height: 4px;\n        -webkit-appearance: none;\n        background: #555;\n        border-radius: 2px;\n        outline: none;\n    }\n    .player-volume input[type="range"]::-webkit-slider-thumb {\n        -webkit-appearance: none;\n        width: 10px;\n        height: 10px;\n        background: #fff;\n        border-radius: 50%;\n        cursor: pointer;\n    }\n    @media (max-width: 768px) {\n        #gallery-player {\n            padding: 0 12px;\n        }\n        .player-volume {\n            display: none;\n        }\n        .player-info {\n            width: auto;\n            max-width: 120px;\n        }\n        .player-progress {\n            margin: 0 12px;\n        }\n    }\n')
        __M_writer('</style>\n')
        if len(translations) > 1:
            pass
            for langname in translations.keys():
                pass
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        if post:
            __M_writer('    ')
            __M_writer(str(post_helper.open_graph_metadata(post)))
            __M_writer('\n    ')
            __M_writer(str(post_helper.twitter_card_information(post)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photo_array = context.get('photo_array', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        len = context.get('len', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        folders = context.get('folders', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <div class="gallery-description">\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </div>\n')
        __M_writer('\n')
        if folders:
            __M_writer('    <div class="gallery-grid">\n')
            for item in folders:
                __M_writer('        ')

                folder = item[0]
                ftitle = item[1]
                fpost = item[2] if len(item) > 2 else None
                        
                
                __M_writer('\n        <a href="')
                __M_writer(str(folder))
                __M_writer('" class="gallery-card">\n')
                if fpost and fpost.previewimage:
                    __M_writer('            <div class="gallery-card-image">\n                <img src="')
                    __M_writer(str(fpost.previewimage))
                    __M_writer('" alt="')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('" loading="lazy">\n            </div>\n')
                else:
                    __M_writer('            <div class="gallery-card-image gallery-card-placeholder">\n                <span>📷</span>\n            </div>\n')
                __M_writer('            <div class="gallery-card-body">\n                <h2>')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</h2>\n            </div>\n        </a>\n')
            __M_writer('    </div>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" loading="lazy" /></a>\n')
            __M_writer('</ul>\n</noscript>\n\n')
            if post and post.meta('music'):

                music_meta = post.meta('music')
                music_files = [f.strip() for f in music_meta.split(',') if f.strip()]
                playlist = []
                for f in music_files:
                    name = f.split('/')[-1]
                    track_title = name.rsplit('.', 1)[0] if '.' in name else name
                    # 把绝对路径 /assets/... 转为相对路径 ../../assets/...，兼容子目录部署
                    if f.startswith('/'):
                        relative_src = '../../' + f.lstrip('/')
                    else:
                        relative_src = f
                    encoded_src = quote(relative_src, safe='/')
                    playlist.append({'src': encoded_src, 'title': track_title})
                
                
                __M_writer('\n<div id="gallery-player">\n    <div class="player-info">\n        <div class="player-cover">🎵</div>\n        <div class="player-meta">\n            <div class="player-title" id="player-title">-</div>\n            <div class="player-artist" id="player-artist">')
                __M_writer(str(len(playlist)))
                __M_writer(' 首歌曲</div>\n        </div>\n    </div>\n    <div class="player-controls">\n        <button class="player-btn" id="player-prev" title="上一首">⏮</button>\n        <button class="player-btn player-play" id="player-play" title="播放/暂停">▶</button>\n        <button class="player-btn" id="player-next" title="下一首">⏭</button>\n    </div>\n    <div class="player-progress">\n        <span class="player-time" id="player-current">0:00</span>\n        <input type="range" id="player-seek" value="0" min="0" max="100">\n        <span class="player-time" id="player-duration">0:00</span>\n    </div>\n    <div class="player-volume">\n        <span>🔊</span>\n        <input type="range" id="player-volume" value="80" min="0" max="100">\n    </div>\n    <audio id="player-audio" preload="metadata"></audio>\n</div>\n<script>\n    window.galleryPlaylist = ')
                __M_writer(str(json.dumps(playlist)))
                __M_writer(';\n</script>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photo_array = context.get('photo_array', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        post = context.get('post', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script src="/assets/js/gallery.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\nrenderGallery(jsonContent, thumbnailSize);\nwindow.addEventListener('resize', function(){renderGallery(jsonContent, thumbnailSize)});\n\n")
        if photo_array and post and post.meta('music'):
            __M_writer("// 底部音乐播放器（仅在单相册页且配置了 music 元数据时生效）\n(function() {\n    const playlist = window.galleryPlaylist;\n    if (!playlist || !playlist.length) return;\n\n    document.body.classList.add('has-gallery-player');\n\n    const audio = document.getElementById('player-audio');\n    const playBtn = document.getElementById('player-play');\n    const prevBtn = document.getElementById('player-prev');\n    const nextBtn = document.getElementById('player-next');\n    const seek = document.getElementById('player-seek');\n    const volume = document.getElementById('player-volume');\n    const currentEl = document.getElementById('player-current');\n    const durationEl = document.getElementById('player-duration');\n    const titleEl = document.getElementById('player-title');\n\n    let currentIndex = 0;\n\n    function formatTime(t) {\n        if (!t || isNaN(t)) return '0:00';\n        const m = Math.floor(t / 60);\n        const s = Math.floor(t % 60).toString().padStart(2, '0');\n        return m + ':' + s;\n    }\n\n    function loadTrack(index) {\n        currentIndex = index;\n        const track = playlist[currentIndex];\n        audio.src = track.src;\n        titleEl.textContent = track.title;\n        durationEl.textContent = '0:00';\n        seek.value = 0;\n        currentEl.textContent = '0:00';\n        playBtn.textContent = '▶️';\n    }\n\n    playBtn.addEventListener('click', function() {\n        if (audio.paused) {\n            if (!audio.src) loadTrack(0);\n            audio.play().catch(function(e) {\n                console.log('播放失败，请检查音频文件是否存在:', e);\n            });\n            playBtn.textContent = '⏸';\n        } else {\n            audio.pause();\n            playBtn.textContent = '▶️';\n        }\n    });\n\n    prevBtn.addEventListener('click', function() {\n        let index = currentIndex - 1;\n        if (index < 0) index = playlist.length - 1;\n        loadTrack(index);\n        audio.play().catch(function() {});\n        playBtn.textContent = '⏸';\n    });\n\n    nextBtn.addEventListener('click', function() {\n        let index = currentIndex + 1;\n        if (index >= playlist.length) index = 0;\n        loadTrack(index);\n        audio.play().catch(function() {});\n        playBtn.textContent = '⏸';\n    });\n\n    audio.addEventListener('timeupdate', function() {\n        if (audio.duration) {\n            seek.value = (audio.currentTime / audio.duration) * 100;\n            currentEl.textContent = formatTime(audio.currentTime);\n        }\n    });\n\n    audio.addEventListener('loadedmetadata', function() {\n        durationEl.textContent = formatTime(audio.duration);\n    });\n\n    audio.addEventListener('ended', function() {\n        nextBtn.click();\n    });\n\n    function seekAudio() {\n        if (audio.duration) {\n            audio.currentTime = (seek.value / 100) * audio.duration;\n        }\n    }\n    seek.addEventListener('input', seekAudio);\n    seek.addEventListener('change', seekAudio);\n\n    volume.addEventListener('input', function() {\n        audio.volume = volume.value / 100;\n    });\n\n    audio.volume = volume.value / 100;\n    loadTrack(0);\n})();\n")
        __M_writer('</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 3, "19": 4, "27": 5, "30": 6, "33": 7, "39": 0, "71": 2, "72": 3, "73": 4, "74": 5, "75": 6, "76": 7, "81": 8, "86": 168, "91": 266, "96": 376, "102": 8, "113": 10, "128": 10, "129": 11, "130": 11, "131": 19, "132": 20, "133": 156, "134": 157, "136": 158, "138": 159, "139": 160, "140": 160, "141": 160, "142": 160, "143": 160, "144": 164, "145": 165, "146": 165, "147": 165, "148": 166, "149": 166, "155": 170, "172": 170, "173": 171, "174": 171, "175": 172, "176": 173, "177": 173, "178": 173, "179": 175, "180": 176, "181": 177, "182": 177, "183": 180, "184": 181, "185": 182, "186": 183, "187": 184, "188": 184, "189": 185, "190": 186, "191": 187, "192": 188, "193": 189, "194": 188, "195": 189, "196": 189, "197": 190, "198": 191, "199": 192, "200": 192, "201": 192, "202": 192, "203": 194, "204": 195, "205": 199, "206": 200, "207": 200, "208": 204, "209": 206, "210": 208, "211": 209, "212": 211, "213": 212, "214": 212, "215": 212, "216": 212, "217": 212, "218": 213, "219": 213, "220": 213, "221": 213, "222": 215, "223": 218, "224": 219, "225": 220, "226": 221, "227": 222, "228": 223, "229": 224, "230": 225, "231": 226, "232": 227, "233": 228, "234": 229, "235": 230, "236": 231, "237": 232, "238": 233, "239": 234, "240": 233, "241": 239, "242": 239, "243": 259, "244": 259, "245": 263, "246": 264, "247": 264, "248": 264, "254": 268, "264": 268, "265": 272, "266": 272, "267": 273, "268": 273, "269": 277, "270": 278, "271": 375, "277": 271}}
__M_END_METADATA
"""
