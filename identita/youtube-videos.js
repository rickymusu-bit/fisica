(() => {
  document.querySelectorAll('[data-youtube-video]').forEach(player => {
    const id = player.dataset.youtubeVideo;
    const stage = player.querySelector('.youtube-stage');
    const button = player.querySelector('[data-youtube-load]');
    const stop = player.querySelector('[data-youtube-stop]');
    const notice = player.querySelector('[data-youtube-notice]');
    if (!/^[\w-]{11}$/.test(id) || !stage || !button || !stop || !notice) return;
    const initialNotice = notice.textContent;
    button.hidden = false;
    button.addEventListener('click', () => {
      if (stage.querySelector('iframe')) return;
      if (navigator.onLine === false) {
        notice.textContent = player.dataset.youtubeOffline;
        return;
      }
      const url = new URL('https://www.youtube-nocookie.com/embed/' + id);
      url.searchParams.set('autoplay', '0');
      url.searchParams.set('playsinline', '1');
      url.searchParams.set('rel', '0');
      const start = Number(player.dataset.youtubeStart || 0);
      if (Number.isSafeInteger(start) && start > 0) url.searchParams.set('start', String(start));
      const frame = document.createElement('iframe');
      frame.src = url.href;
      frame.title = player.dataset.youtubeTitle;
      frame.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.allow = 'encrypted-media; fullscreen; picture-in-picture';
      frame.allowFullscreen = true;
      frame.setAttribute('tabindex', '0');
      button.hidden = true;
      stage.append(frame);
      stop.hidden = false;
      notice.textContent = player.dataset.youtubeLoaded;
      frame.focus();
    });
    stop.addEventListener('click', () => {
      stage.querySelector('iframe')?.remove();
      stop.hidden = true;
      button.hidden = false;
      notice.textContent = initialNotice;
      button.focus();
    });
  });
})();
