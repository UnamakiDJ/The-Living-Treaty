// timeline.js
// Simple interactive timeline logic for The Living Treaty.

(function () {
  const eraFilterEl = document.getElementById("eraFilter");
  const tagFilterEl = document.getElementById("tagFilter");
  const sortDirectionEl = document.getElementById("sortDirection");
  const timelineListEl = document.getElementById("timelineList");
  const eventDetailEl = document.getElementById("eventDetail");

  let currentActiveId = null;

  function initFilters() {
    const eras = new Set();
    const tags = new Set();

    TIMELINE_EVENTS.forEach((evt) => {
      eras.add(evt.era);
      evt.tags.forEach((tag) => tags.add(tag));
    });

    // Populate era filter
    [...eras].sort().forEach((era) => {
      const opt = document.createElement("option");
      opt.value = era;
      opt.textContent = era;
      eraFilterEl.appendChild(opt);
    });

    // Populate tag filter
    [...tags].sort().forEach((tag) => {
      const opt = document.createElement("option");
      opt.value = tag;
      opt.textContent = tag;
      tagFilterEl.appendChild(opt);
    });

    eraFilterEl.addEventListener("change", renderTimeline);
    tagFilterEl.addEventListener("change", renderTimeline);
    sortDirectionEl.addEventListener("change", renderTimeline);
  }

  function getFilteredAndSortedEvents() {
    const era = eraFilterEl.value;
    const tag = tagFilterEl.value;
    const direction = sortDirectionEl.value;

    let events = TIMELINE_EVENTS.slice();

    if (era !== "all") {
      events = events.filter((e) => e.era === era);
    }
    if (tag !== "all") {
      events = events.filter((e) => e.tags.includes(tag));
    }

    events.sort((a, b) =>
      direction === "asc" ? a.sortKey - b.sortKey : b.sortKey - a.sortKey
    );

    return events;
  }

  function renderTimeline() {
    const events = getFilteredAndSortedEvents();

    timelineListEl.innerHTML = "";

    if (!events.length) {
      const empty = document.createElement("p");
      empty.className = "timeline-empty";
      empty.textContent =
        "No events match those filters yet. Try a different era or tag.";
      timelineListEl.appendChild(empty);
      eventDetailEl.innerHTML = `
        <div class="detail-placeholder">
          <h2>No events found</h2>
          <p>Try changing the filters to see more of the story of Mi’kma’ki.</p>
        </div>
      `;
      currentActiveId = null;
      return;
    }

    events.forEach((evt) => {
      const card = document.createElement("article");
      card.className = "timeline-event";
      card.dataset.eventId = evt.id;

      const header = document.createElement("div");
      header.className = "timeline-event-header";

      const title = document.createElement("div");
      title.className = "timeline-event-title";
      title.textContent = evt.title;

      const date = document.createElement("div");
      date.className = "timeline-event-date";
      date.textContent = evt.dateDisplay;

      header.appendChild(title);
      header.appendChild(date);

      const meta = document.createElement("div");
      meta.className = "timeline-event-meta";

      const eraBadge = document.createElement("span");
      eraBadge.className = "badge badge-era";
      eraBadge.textContent = evt.era;

      const typeBadge = document.createElement("span");
      typeBadge.className = "badge badge-type";
      typeBadge.textContent = evt.type;

      meta.appendChild(eraBadge);
      meta.appendChild(typeBadge);

      evt.tags.forEach((t) => {
        const tagBadge = document.createElement("span");
        tagBadge.className = "badge";
        tagBadge.textContent = t;
        meta.appendChild(tagBadge);
      });

      card.appendChild(header);
      card.appendChild(meta);

      card.addEventListener("click", () => {
        setActiveEvent(evt.id);
      });

      if (evt.id === currentActiveId) {
        card.classList.add("active");
      }

      timelineListEl.appendChild(card);
    });

    // If nothing selected yet, pick the first in the list
    if (!currentActiveId && events.length) {
      setActiveEvent(events[0].id);
    } else {
      // Re-highlight current active if still in filtered list
      highlightActiveCard();
    }
  }

  function highlightActiveCard() {
    const cards = timelineListEl.querySelectorAll(".timeline-event");
    cards.forEach((card) => {
      if (card.dataset.eventId === currentActiveId) {
        card.classList.add("active");
      } else {
        card.classList.remove("active");
      }
    });
  }

  function setActiveEvent(eventId) {
    currentActiveId = eventId;
    highlightActiveCard();

    const evt = TIMELINE_EVENTS.find((e) => e.id === eventId);
    if (!evt) return;

    eventDetailEl.innerHTML = "";

    const container = document.createElement("div");

    const title = document.createElement("h2");
    title.textContent = evt.title;

    const date = document.createElement("div");
    date.className = "detail-date";
    date.textContent = `${evt.dateDisplay} • ${evt.era} • ${evt.type}`;

    container.appendChild(title);
    container.appendChild(date);

    // Western lens
    if (evt.westernSummary) {
      const h = document.createElement("h3");
      h.className = "detail-section-title";
      h.textContent = "Western historical / scientific lens";
      const p = document.createElement("p");
      p.textContent = evt.westernSummary;
      container.appendChild(h);
      container.appendChild(p);
    }

    // L’nuk lens
    if (evt.lnukSummary) {
      const h = document.createElement("h3");
      h.className = "detail-section-title";
      h.textContent = "L’nuk (Mi’kmaw) lens";
      const p = document.createElement("p");
      p.textContent = evt.lnukSummary;
      container.appendChild(h);
      container.appendChild(p);
    }

    // Two-Eyed Seeing reflection
    if (evt.twoEyedReflection) {
      const h = document.createElement("h3");
      h.className = "detail-section-title";
      h.textContent = "Two-Eyed Seeing";
      const p = document.createElement("p");
      p.textContent = evt.twoEyedReflection;
      container.appendChild(h);
      container.appendChild(p);
    }

    // People
    if (evt.people && evt.people.length) {
      const h = document.createElement("h3");
      h.className = "detail-section-title";
      h.textContent = "Key L’nuk figures";

      const list = document.createElement("ul");
      list.className = "people-list";

      evt.people.forEach((person) => {
        const li = document.createElement("li");
        li.className = "people-card";

        const name = document.createElement("h3");
        name.textContent = person.name;

        const role = document.createElement("div");
        role.className = "role";
        role.textContent = person.role || "";

        const bio = document.createElement("p");
        bio.textContent = person.bio || "";

        li.appendChild(name);
        li.appendChild(role);
        li.appendChild(bio);

        list.appendChild(li);
      });

      container.appendChild(h);
      container.appendChild(list);
    }

    eventDetailEl.appendChild(container);
  }

  // Boot it up
  document.addEventListener("DOMContentLoaded", () => {
    initFilters();
    renderTimeline();
  });
})();
