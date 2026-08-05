/*
  LLA_MEDIA, single source of truth for the Video tabs (Julie / Courtney / Omri).
  Every tab builds its DOM from this object at load time. Add new cuts,
  storyboards, or resize renders by editing ONLY this file.

  Shape:
  window.LLA_MEDIA = {
    julie:    { cuts: [{label, src, poster, duration, w, h, bytes}], storyboards: [{label, src, pages}] },
    courtney: { cuts: [...], storyboards: [...] },
    omri:     { julie: [{placement, label, src, w, h, bytes, duration, codec, audio}], courtney: [...] }
  }

  Paths are relative to /home/user/workspace/src/gallery, where this file is
  loaded from alongside index.html. Every entry below was verified with
  ffprobe / pdfinfo against the staged files in src/gallery/media before
  being listed. Nothing here is invented.
*/
window.LLA_MEDIA = {
  julie: {
    // Julie's cuts are still in production. Left empty on purpose so the tab
    // renders its structure with zero fabricated entries.
    cuts: [],
    storyboards: []
  },

  courtney: {
    cuts: [
      {
        label: "101s Master",
        src: "media/courtney/LLA-Courtney-101s-Master.mp4",
        poster: "media/courtney/poster_101s.jpg",
        duration: 101.10,
        w: 1920,
        h: 1080,
        fps: 30,
        bytes: 87561367,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA-Courtney-101s-Master.mp4"
      },
      {
        label: "90s Cut",
        src: "media/courtney/LLA-Courtney-90s-Cut.mp4",
        poster: "media/courtney/poster_90s.jpg",
        duration: 95.20,
        w: 1920,
        h: 1080,
        fps: 30,
        bytes: 82422453,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA-Courtney-90s-Cut.mp4"
      }
    ],
    storyboards: [
      {
        label: "Storyboard, 101s Master",
        src: "media/courtney/Storyboard-101s.pdf",
        pages: 7,
        bytes: 6264830,
        filename: "Storyboard-101s.pdf"
      },
      {
        label: "Storyboard, 95s Cut",
        src: "media/courtney/Storyboard-95s.pdf",
        pages: 6,
        bytes: 6210647,
        filename: "Storyboard-95s.pdf"
      }
    ],
    proof: {
      label: "Lipsync Proof",
      src: "media/courtney/Lipsync-Proof.png",
      w: 2060,
      h: 570,
      bytes: 1158564,
      filename: "Lipsync-Proof.png"
    }
  },

  omri: {
    // Meta / Instagram resize pack, 90s cut, per talent. Only resizes that
    // exist on disk right now are listed. New sizes drop in as they render.
    julie: [],
    courtney: [
      {
        placement: "Feed square",
        label: "1080 x 1080",
        src: "media/omri/LLA_Courtney_90s_1x1_1080x1080.mp4",
        poster: "media/omri/LLA_Courtney_90s_1x1_1080x1080_poster.jpg",
        w: 1080,
        h: 1080,
        duration: 95.10,
        bytes: 22306719,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA_Courtney_90s_1x1_1080x1080.mp4",
        safeZone: "Feed square has no UI overlay. Keep roughly 100px of padding on every side so the subject reads clearly at the 880x880 working area Meta recommends."
      },
      {
        placement: "Feed vertical, highest reach placement",
        label: "1080 x 1350",
        src: "media/omri/LLA_Courtney_90s_4x5_1080x1350.mp4",
        poster: "media/omri/LLA_Courtney_90s_4x5_1080x1350_poster.jpg",
        w: 1080,
        h: 1350,
        duration: 95.10,
        bytes: 23737611,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA_Courtney_90s_4x5_1080x1350.mp4",
        safeZone: "Feed vertical has no UI overlay, but Meta recommends roughly 250px of padding top and bottom so headline and CTA text sit inside the 880x850 working area."
      },
      {
        placement: "Reels and Stories",
        label: "1080 x 1920",
        src: "media/omri/LLA_Courtney_90s_9x16_1080x1920.mp4",
        poster: "media/omri/LLA_Courtney_90s_9x16_1080x1920_poster.jpg",
        w: 1080,
        h: 1920,
        duration: 95.10,
        bytes: 27090590,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA_Courtney_90s_9x16_1080x1920.mp4",
        safeZone: "Meta's unified 2026 safe zone for Reels and Stories keeps the top 270px clear for the profile picture and timestamp, and the bottom 670px clear of the like, comment, share, save, audio, and caption stack. Center safe area is 950x980."
      },
      {
        placement: "In-stream and desktop feed",
        label: "1920 x 1080",
        src: "media/omri/LLA_Courtney_90s_16x9_1920x1080.mp4",
        poster: "media/omri/LLA_Courtney_90s_16x9_1920x1080_poster.jpg",
        w: 1920,
        h: 1080,
        duration: 95.10,
        bytes: 50418392,
        codec: "h264",
        audio: "AAC stereo 48kHz",
        filename: "LLA_Courtney_90s_16x9_1920x1080.mp4",
        safeZone: "In-stream and desktop feed run full width with no platform UI overlay. Keep on-screen text inside the center 90 percent so nothing sits at the extreme edge on wider or narrower player crops."
      }
    ]
  }
};
