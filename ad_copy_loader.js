/*
  Loads build/ad_copy.json into window.LLA_ADCOPY as soon as it is available.
  The Omri tab listens for the lla-adcopy-loaded event and re-renders once
  this resolves, so the ad copy block fills in automatically whether the
  file exists at page load or arrives later.
*/
(function(){
  function load(){
    fetch('ad_copy.json', { cache: 'no-store' })
      .then(function(res){
        if (!res.ok) throw new Error('ad_copy.json not ready');
        return res.json();
      })
      .then(function(json){
        window.LLA_ADCOPY = json;
        window.dispatchEvent(new CustomEvent('lla-adcopy-loaded'));
      })
      .catch(function(){
        // ad_copy.json not present yet, the Omri tab renders its
        // own structured empty state and will retry is not needed
        // since the owning agent will ship the file and a page
        // reload will pick it up.
      });
  }
  load();
})();
