/** @tele-module **/

import { registry } from '@web/core/registry'
import { HotkeyCommandItem } from '@web/core/commands/default_providers'

// The only way to know if an editor is under focus when the command palette
// open is to look if there in a selection within a wysiwyg editor in the page.
// As the selection changes after the command palette is open, we need to save
// the action (that have the range and editor in the closure) as well as the
// label to use.
let sessionActionLabel = [];

const commandProviderRegistry = registry.category("command_provider");
commandProviderRegistry.add("link dialog", {
    async provide(env, { sessionId }) {
        const Wysiwyg = tele.__DEBUG__.services['web_editor.wysiwyg'];
        if (!Wysiwyg) {
            return [];
        }
        let [lastSessionId, action, label] = sessionActionLabel;
        if (lastSessionId !== sessionId) {
            const wysiwyg = [...Wysiwyg.activeWysiwygs].find((wysiwyg) => {
                return wysiwyg.isSelectionInEditable();
            });
            const selection = wysiwyg && wysiwyg.teleEditor && wysiwyg.teleEditor.document.getSelection();
            const range = selection && selection.rangeCount && selection.getRangeAt(0);
            if (range) {
                label = !wysiwyg.getInSelection('a') ? 'Create link' : 'Edit link';
                action = () => {
                    const selection = wysiwyg.teleEditor.document.getSelection();
                    selection.removeAllRanges();
                    selection.addRange(range);

                    wysiwyg.openLinkToolsFromSelection();
                }
                sessionActionLabel = [sessionId, action, label]
            } else {
                sessionActionLabel = [sessionId];
            }
        }
        [lastSessionId, action, label] = sessionActionLabel;

        if (action) {
            return [
                {
                    Component: HotkeyCommandItem,
                    action: action,
                    category: 'shortcut_conflict',
                    name: label,
                    props: { hotkey: 'control+k' },
                }
            ]
        } else {
            return [];
        }
    },
});
