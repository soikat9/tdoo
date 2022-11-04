/** @tele-module **/

import { insert, insertAndReplace, link, replace } from '@mail/model/model_field_command';
import { makeDeferred } from '@mail/utils/deferred/deferred';
import {
    afterEach,
    afterNextRender,
    beforeEach,
    createRootMessagingComponent,
    nextAnimationFrame,
    start,
} from '@mail/utils/test_utils';

import Bus from 'web.Bus';

QUnit.module('mail', {}, function () {
QUnit.module('components', {}, function () {
QUnit.module('message', {}, function () {
QUnit.module('message_tests.js', {
    beforeEach() {
        beforeEach(this);

        this.start = async params => {
            const res = await start({ ...params, data: this.data });
            const { afterEvent, components, env, widget } = res;
            this.afterEvent = afterEvent;
            this.components = components;
            this.env = env;
            this.widget = widget;
            return res;
        };
    },
    afterEach() {
        afterEach(this);
    },
});

QUnit.test('basic rendering', async function (assert) {
    assert.expect(12);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        author: insert({ id: 7, display_name: "Demo User" }),
        body: "<p>Test</p>",
        date: moment(),
        id: 100,
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelectorAll('.o_Message').length,
        1,
        "should display a message component"
    );
    const messageEl = document.querySelector('.o_Message');
    assert.strictEqual(
        messageEl.dataset.messageLocalId,
        this.messaging.models['mail.message'].findFromIdentifyingData({ id: 100 }).localId,
        "message component should be linked to message store model"
    );
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_Message_sidebar`).length,
        1,
        "message should have a sidebar"
    );
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_Message_sidebar .o_Message_authorAvatar`).length,
        1,
        "message should have author avatar in the sidebar"
    );
    assert.strictEqual(
        messageEl.querySelector(`:scope .o_Message_authorAvatar`).tagName,
        'IMG',
        "message author avatar should be an image"
    );
    assert.strictEqual(
        messageEl.querySelector(`:scope .o_Message_authorAvatar`).dataset.src,
        '/web/image/res.partner/7/avatar_128',
        "message author avatar should GET image of the related partner"
    );
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_Message_authorName`).length,
        1,
        "message should display author name"
    );
    assert.strictEqual(
        messageEl.querySelector(`:scope .o_Message_authorName`).textContent,
        "Demo User",
        "message should display correct author name"
    );
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_Message_date`).length,
        1,
        "message should display date"
    );
    await afterNextRender(() => messageEl.click());
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_MessageActionList`).length,
        1,
        "message should display list of actions"
    );
    assert.strictEqual(
        messageEl.querySelectorAll(`:scope .o_Message_content`).length,
        1,
        "message should display the content"
    );
    assert.strictEqual(
        messageEl.querySelector(`:scope .o_Message_prettyBody`).innerHTML,
        "<p>Test</p>",
        "message should display the correct content"
    );
});

QUnit.test('Notification Sent', async function (assert) {
    assert.expect(9);

    this.data['res.partner'].records.push({ id: 12, name: "Someone", partner_share: true });
    this.data['mail.channel'].records.push({ id: 11 });
    this.data['mail.message'].records.push({
        body: 'not empty',
        id: 10,
        message_type: 'email',
        model: 'mail.channel',
        res_id: 11,
    });
    this.data['mail.notification'].records.push({
        id: 11,
        mail_message_id: 10,
        notification_status: 'sent',
        notification_type: 'email',
        res_partner_id: 12,
    });
    const { createThreadViewComponent } = await this.start();
    const thread = this.messaging.models['mail.thread'].findFromIdentifyingData({
        id: 11,
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_notificationIconClickable',
        "should display the notification icon container"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_notificationIcon',
        "should display the notification icon"
    );
    assert.hasClass(
        document.querySelector('.o_Message_notificationIcon'),
        'fa-envelope-o',
        "icon should represent email success"
    );

    await afterNextRender(() => {
        document.querySelector('.o_Message_notificationIconClickable').click();
    });
    assert.containsOnce(
        document.body,
        '.o_NotificationPopover',
        "notification popover should be open"
    );
    assert.containsOnce(
        document.body,
        '.o_NotificationPopover_notificationIcon',
        "popover should have one icon"
    );
    assert.hasClass(
        document.querySelector('.o_NotificationPopover_notificationIcon'),
        'fa-check',
        "popover should have the sent icon"
    );
    assert.containsOnce(
        document.body,
        '.o_NotificationPopover_notificationPartnerName',
        "popover should have the partner name"
    );
    assert.strictEqual(
        document.querySelector('.o_NotificationPopover_notificationPartnerName').textContent.trim(),
        "Someone",
        "partner name should be correct"
    );
});

QUnit.test('Notification Error', async function (assert) {
    assert.expect(8);

    const openResendActionDef = makeDeferred();
    const bus = new Bus();
    bus.on('do-action', null, payload => {
        assert.step('do_action');
        assert.strictEqual(
            payload.action,
            'mail.mail_resend_message_action',
            "action should be the one to resend email"
        );
        assert.strictEqual(
            payload.options.additional_context.mail_message_to_resend,
            10,
            "action should have correct message id"
        );
        openResendActionDef.resolve();
    });

    this.data['res.partner'].records.push({ id: 12, name: "Someone", partner_share: true });
    this.data['mail.channel'].records.push({ id: 11 });
    this.data['mail.message'].records.push({
        body: 'not empty',
        id: 10,
        message_type: 'email',
        model: 'mail.channel',
        res_id: 11,
    });
    this.data['mail.notification'].records.push({
        id: 11,
        mail_message_id: 10,
        notification_status: 'exception',
        notification_type: 'email',
        res_partner_id: 12,
    });
    const { createThreadViewComponent } = await this.start({ env: { bus } });
    const thread = this.messaging.models['mail.thread'].findFromIdentifyingData({
        id: 11,
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_notificationIconClickable',
        "should display the notification icon container"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_notificationIcon',
        "should display the notification icon"
    );
    assert.hasClass(
        document.querySelector('.o_Message_notificationIcon'),
        'fa-envelope',
        "icon should represent email error"
    );
    document.querySelector('.o_Message_notificationIconClickable').click();
    await openResendActionDef;
    assert.verifySteps(
        ['do_action'],
        "should do an action to display the resend email dialog"
    );
});

QUnit.test("'channel_fetch' notification received is correctly handled", async function (assert) {
    assert.expect(3);

    this.data['res.partner'].records.push({
        display_name: "Recipient",
        id: 11,
    });
    this.data['mail.channel'].records.push({
        channel_type: 'chat',
        id: 11,
        members: [this.data.currentPartnerId, 11],
    });
    const { createThreadViewComponent } = await this.start();
    const currentPartner = this.messaging.models['mail.partner'].insert({
        id: this.messaging.currentPartner.id,
        display_name: "Demo User",
    });
    const thread = this.messaging.models['mail.thread'].findFromIdentifyingData({
        id: 11,
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    this.messaging.models['mail.message'].create({
        author: link(currentPartner),
        body: "<p>Test</p>",
        id: 100,
        originThread: link(thread),
    });

    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsNone(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message component should not have any check (V) as message is not yet received"
    );

    // Simulate received channel fetched notification
    await afterNextRender(() => {
        this.widget.call('bus_service', 'trigger', 'notification', [{
            type: 'mail.channel.partner/fetched',
            payload: {
                channel_id: 11,
                last_message_id: 100,
                partner_id: 11,
            },
    }]);
    });

    assert.containsOnce(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message seen indicator component should only contain one check (V) as message is just received"
    );
});

QUnit.test("'channel_seen' notification received is correctly handled", async function (assert) {
    assert.expect(3);

    this.data['res.partner'].records.push({
        display_name: "Recipient",
        id: 11,
    });
    this.data['mail.channel'].records.push({
        channel_type: 'chat',
        id: 11,
        members: [this.data.currentPartnerId, 11],
    });
    const { createThreadViewComponent } = await this.start();
    const currentPartner = this.messaging.models['mail.partner'].insert({
        id: this.messaging.currentPartner.id,
        display_name: "Demo User",
    });
    const thread = this.messaging.models['mail.thread'].findFromIdentifyingData({
        id: 11,
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    this.messaging.models['mail.message'].create({
        author: link(currentPartner),
        body: "<p>Test</p>",
        id: 100,
        originThread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsNone(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message component should not have any check (V) as message is not yet received"
    );

    // Simulate received channel seen notification
    await afterNextRender(() => {
        this.widget.call('bus_service', 'trigger', 'notification', [{
            type: 'mail.channel.partner/seen',
            payload: {
                channel_id: 11,
                last_message_id: 100,
                partner_id: 11,
            },
        }]);
    });
    assert.containsN(
        document.body,
        '.o_MessageSeenIndicator_icon',
        2,
        "message seen indicator component should contain two checks (V) as message is seen"
    );
});

QUnit.test("'channel_fetch' notification then 'channel_seen' received  are correctly handled", async function (assert) {
    assert.expect(4);

    this.data['res.partner'].records.push({
        display_name: "Recipient",
        id: 11,
    });
    this.data['mail.channel'].records.push({
        channel_type: 'chat',
        id: 11,
        members: [this.data.currentPartnerId, 11],
    });
    const { createThreadViewComponent } = await this.start();
    const currentPartner = this.messaging.models['mail.partner'].insert({
        id: this.messaging.currentPartner.id,
        display_name: "Demo User",
    });
    const thread = this.messaging.models['mail.thread'].findFromIdentifyingData({
        id: 11,
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    this.messaging.models['mail.message'].create({
        author: link(currentPartner),
        body: "<p>Test</p>",
        id: 100,
        originThread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsNone(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message component should not have any check (V) as message is not yet received"
    );

    // Simulate received channel fetched notification
    await afterNextRender(() => {
        this.widget.call('bus_service', 'trigger', 'notification', [{
            type: 'mail.channel.partner/fetched',
            payload: {
                channel_id: 11,
                last_message_id: 100,
                partner_id: 11,
            }
        }]);
    });
    assert.containsOnce(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message seen indicator component should only contain one check (V) as message is just received"
    );

    // Simulate received channel seen notification
    await afterNextRender(() => {
        this.widget.call('bus_service', 'trigger', 'notification', [{
            type: 'mail.channel.partner/seen',
            payload: {
                channel_id: 11,
                last_message_id: 100,
                partner_id: 11,
            },
        }]);
    });
    assert.containsN(
        document.body,
        '.o_MessageSeenIndicator_icon',
        2,
        "message seen indicator component should contain two checks (V) as message is now seen"
    );
});

QUnit.test('do not show messaging seen indicator if not authored by me', async function (assert) {
    assert.expect(2);

    const { createThreadViewComponent } = await this.start();
    const author = this.messaging.models['mail.partner'].create({
        id: 100,
        display_name: "Demo User"
    });
    const thread = this.messaging.models['mail.thread'].create({
        channel_type: 'chat',
        id: 11,
        partnerSeenInfos: insertAndReplace([
            {
                lastFetchedMessage: insert({ id: 100 }),
                partner: replace(this.messaging.currentPartner),
            },
            {
                lastFetchedMessage: insert({ id: 100 }),
                partner: replace(author),
            },
        ]),
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    this.messaging.models['mail.message'].insert({
        author: link(author),
        body: "<p>Test</p>",
        id: 100,
        originThread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsNone(
        document.body,
        '.o_Message_seenIndicator',
        "message component should not have any message seen indicator"
    );
});

QUnit.test('do not show messaging seen indicator if before last seen by all message', async function (assert) {
    assert.expect(3);

    await this.start();
    const currentPartner = this.messaging.models['mail.partner'].insert({
        id: this.messaging.currentPartner.id,
        display_name: "Demo User",
    });
    const thread = this.messaging.models['mail.thread'].create({
        channel_type: 'chat',
        id: 11,
        messageSeenIndicators: insertAndReplace({
            message: insertAndReplace({ id: 99 }),
        }),
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    const lastSeenMessage = this.messaging.models['mail.message'].create({
        author: link(currentPartner),
        body: "<p>You already saw me</p>",
        id: 100,
        originThread: link(thread),
    });
    this.messaging.models['mail.message'].insert({
        author: link(currentPartner),
        body: "<p>Test</p>",
        id: 99,
        originThread: link(thread),
    });
    this.messaging.models['mail.thread_partner_seen_info'].insert([
        {
            lastSeenMessage: link(lastSeenMessage),
            partner: replace(this.messaging.currentPartner),
            thread: replace(thread),
        },
        {
            lastSeenMessage: link(lastSeenMessage),
            partner: insertAndReplace({ id: 100 }),
            thread: replace(thread),
        },
    ]);
    await createRootMessagingComponent(this, "Message", {
        props: { messageViewLocalId: threadViewer.threadView.messageViews[0].localId },
        target: this.widget.el,
    });

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_seenIndicator',
        "message component should have a message seen indicator"
    );
    assert.containsNone(
        document.body,
        '.o_MessageSeenIndicator_icon',
        "message component should not have any check (V)"
    );
});

QUnit.test('only show messaging seen indicator if authored by me, after last seen by all message', async function (assert) {
    assert.expect(3);

    const { createThreadViewComponent } = await this.start();
    const currentPartner = this.messaging.models['mail.partner'].insert({
        id: this.messaging.currentPartner.id,
        display_name: "Demo User"
    });
    const thread = this.messaging.models['mail.thread'].create({
        channel_type: 'chat',
        id: 11,
        partnerSeenInfos: insertAndReplace([
            {
                lastSeenMessage: insert({ id: 100 }),
                partner: replace(this.messaging.currentPartner),
            },
            {
                lastFetchedMessage: insert({ id: 100 }),
                lastSeenMessage: insert({ id: 99 }),
                partner: insertAndReplace({ id: 100 }),
            },
        ]),
        messageSeenIndicators: insertAndReplace({
            message: insertAndReplace({ id: 100 }),
        }),
        model: 'mail.channel',
    });
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    this.messaging.models['mail.message'].insert({
        author: link(currentPartner),
        body: "<p>Test</p>",
        id: 100,
        originThread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);

    assert.containsOnce(
        document.body,
        '.o_Message',
        "should display a message component"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_seenIndicator',
        "message component should have a message seen indicator"
    );
    assert.containsN(
        document.body,
        '.o_MessageSeenIndicator_icon',
        1,
        "message component should have one check (V) because the message was fetched by everyone but no other member than author has seen the message"
    );
});

QUnit.test('allow attachment delete on authored message', async function (assert) {
    assert.expect(5);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        attachments: insertAndReplace({
            filename: "BLAH.jpg",
            id: 10,
            name: "BLAH",
            mimetype: 'image/jpeg',
        }),
        author: link(this.messaging.currentPartner),
        body: "<p>Test</p>",
        id: 100,
    });
    await createMessageComponent(message);

    assert.containsOnce(
        document.body,
        '.o_AttachmentImage',
        "should have an attachment",
    );
    assert.containsOnce(
        document.body,
        '.o_AttachmentImage_actionUnlink',
        "should have delete attachment button"
    );

    await afterNextRender(() => document.querySelector('.o_AttachmentImage_actionUnlink').click());
    assert.containsOnce(
        document.body,
        '.o_AttachmentDeleteConfirmDialog',
        "An attachment delete confirmation dialog should have been opened"
    );
    assert.strictEqual(
        document.querySelector('.o_AttachmentDeleteConfirmDialog_mainText').textContent,
        `Do you really want to delete "BLAH"?`,
        "Confirmation dialog should contain the attachment delete confirmation text"
    );

    await afterNextRender(() =>
        document.querySelector('.o_AttachmentDeleteConfirmDialog_confirmButton').click()
    );
    assert.containsNone(
        document.body,
        '.o_AttachmentCard',
        "should no longer have an attachment",
    );
});

QUnit.test('prevent attachment delete on non-authored message in channels', async function (assert) {
    assert.expect(2);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        attachments: insertAndReplace({
            filename: "BLAH.jpg",
            id: 10,
            name: "BLAH",
            mimetype: 'image/jpeg',
            originThread: insertAndReplace({
                id: 11,
                model: 'mail.channel',
            }),
        }),
        author: insert({ id: 11, display_name: "Guy" }),
        body: "<p>Test</p>",
        id: 100,
    });
    await createMessageComponent(message);

    assert.containsOnce(
        document.body,
        '.o_AttachmentImage',
        "should have an attachment",
    );
    assert.containsNone(
        document.body,
        '.o_AttachmentImage_actionUnlink',
        "delete attachment button should not be printed"
    );
});

QUnit.test('subtype description should be displayed if it is different than body', async function (assert) {
    assert.expect(2);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        body: "<p>Hello</p>",
        id: 100,
        subtype_description: 'Bonjour',
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_content',
        "message should have content"
    );
    assert.strictEqual(
        document.querySelector(`.o_Message_content`).textContent,
        "HelloBonjour",
        "message content should display both body and subtype description when they are different"
    );
});

QUnit.test('subtype description should not be displayed if it is similar to body', async function (assert) {
    assert.expect(2);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        body: "<p>Hello</p>",
        id: 100,
        subtype_description: 'hello',
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_content',
        "message should have content"
    );
    assert.strictEqual(
        document.querySelector(`.o_Message_content`).textContent,
        "Hello",
        "message content should display only body when subtype description is similar"
    );
});

QUnit.test('data-oe-id & data-oe-model link redirection on click', async function (assert) {
    assert.expect(7);

    const bus = new Bus();
    bus.on('do-action', null, payload => {
        assert.strictEqual(
            payload.action.type,
            'ir.actions.act_window',
            "action should open view"
        );
        assert.strictEqual(
            payload.action.res_model,
            'some.model',
            "action should open view on 'some.model' model"
        );
        assert.strictEqual(
            payload.action.res_id,
            250,
            "action should open view on 250"
        );
        assert.step('do-action:openFormView_some.model_250');
    });
    const { createMessageComponent } = await this.start({ env: { bus } });
    const message = this.messaging.models['mail.message'].create({
        body: `<p><a href="#" data-oe-id="250" data-oe-model="some.model">some.model_250</a></p>`,
        id: 100,
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_content',
        "message should have content"
    );
    assert.containsOnce(
        document.querySelector('.o_Message_content'),
        'a',
        "message content should have a link"
    );

    document.querySelector(`.o_Message_content a`).click();
    assert.verifySteps(
        ['do-action:openFormView_some.model_250'],
        "should have open form view on related record after click on link"
    );
});

QUnit.test('chat with author should be opened after clicking on his avatar', async function (assert) {
    assert.expect(4);

    this.data['res.partner'].records.push({ id: 10 });
    this.data['res.users'].records.push({ partner_id: 10 });
    const { createMessageComponent } = await this.start({
        hasChatWindow: true,
    });
    const message = this.messaging.models['mail.message'].create({
        author: insert({ id: 10 }),
        id: 10,
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_authorAvatar',
        "message should have the author avatar"
    );
    assert.hasClass(
        document.querySelector('.o_Message_authorAvatar'),
        'o_redirect',
        "author avatar should have the redirect style"
    );

    await afterNextRender(() =>
        document.querySelector('.o_Message_authorAvatar').click()
    );
    assert.containsOnce(
        document.body,
        '.o_ChatWindow_thread',
        "chat window with thread should be opened after clicking on author avatar"
    );
    assert.strictEqual(
        document.querySelector('.o_ChatWindow_thread').dataset.correspondentId,
        message.author.id.toString(),
        "chat with author should be opened after clicking on his avatar"
    );
});

QUnit.test('chat with author should be opened after clicking on his im status icon', async function (assert) {
    assert.expect(4);

    this.data['res.partner'].records.push({ id: 10 });
    this.data['res.users'].records.push({ partner_id: 10 });
    const { createMessageComponent } = await this.start({
        hasChatWindow: true,
    });
    const message = this.messaging.models['mail.message'].create({
        author: insert({ id: 10, im_status: 'online' }),
        id: 10,
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_partnerImStatusIcon',
        "message should have the author im status icon"
    );
    assert.hasClass(
        document.querySelector('.o_Message_partnerImStatusIcon'),
        'o-has-open-chat',
        "author im status icon should have the open chat style"
    );

    await afterNextRender(() =>
        document.querySelector('.o_Message_partnerImStatusIcon').click()
    );
    assert.containsOnce(
        document.body,
        '.o_ChatWindow_thread',
        "chat window with thread should be opened after clicking on author im status icon"
    );
    assert.strictEqual(
        document.querySelector('.o_ChatWindow_thread').dataset.correspondentId,
        message.author.id.toString(),
        "chat with author should be opened after clicking on his im status icon"
    );
});

QUnit.test('open chat with author on avatar click should be disabled when currently chatting with the author', async function (assert) {
    assert.expect(3);

    this.data['mail.channel'].records.push({
        id: 11,
        channel_type: 'chat',
        members: [this.data.currentPartnerId, 10],
        public: 'private',
    });
    this.data['res.partner'].records.push({ id: 10 });
    this.data['res.users'].records.push({ partner_id: 10 });
    this.data['mail.message'].records.push({
        author_id: 10,
        body: 'not empty',
        id: 10,
        model: 'mail.channel',
        res_id: 11,
    });
    const { createThreadViewComponent } = await this.start({
        hasChatWindow: true,
    });
    const correspondent = this.messaging.models['mail.partner'].insert({ id: 10 });
    const thread = await correspondent.getChat();
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: link(thread),
    });
    await createThreadViewComponent(threadViewer.threadView);
    assert.containsOnce(
        document.body,
        '.o_Message_authorAvatar',
        "message should have the author avatar"
    );
    assert.doesNotHaveClass(
        document.querySelector('.o_Message_authorAvatar'),
        'o_redirect',
        "author avatar should not have the redirect style"
    );

    document.querySelector('.o_Message_authorAvatar').click();
    await nextAnimationFrame();
    assert.containsNone(
        document.body,
        '.o_ChatWindow',
        "should have no thread opened after clicking on author avatar when currently chatting with the author"
    );
});

QUnit.test('basic rendering of tracking value (float type)', async function (assert) {
    assert.expect(8);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "float",
            id: 6,
            new_value: 45.67,
            old_value: 12.3,
        }],
    });
    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValue',
        "should display a tracking value"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueFieldName',
        "should display the name of the tracked field"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueFieldName').textContent,
        "Total:",
        "should display the correct tracked field name (Total)",
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueOldValue',
        "should display the old value"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueOldValue').textContent,
        "12.30",
        "should display the correct old value (12.30)",
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueSeparator',
        "should display the separator"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueNewValue',
        "should display the new value"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueNewValue').textContent,
        "45.67",
        "should display the correct new value (45.67)",
    );
});

QUnit.test('rendering of tracked field of type integer: from non-0 to 0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "integer",
            id: 6,
            new_value: 0,
            old_value: 1,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:10",
        "should display the correct content of tracked field of type integer: from non-0 to 0 (Total: 1 -> 0)"
    );
});

QUnit.test('rendering of tracked field of type integer: from 0 to non-0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "integer",
            id: 6,
            new_value: 1,
            old_value: 0,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:01",
        "should display the correct content of tracked field of type integer: from 0 to non-0 (Total: 0 -> 1)"
    );
});

QUnit.test('rendering of tracked field of type float: from non-0 to 0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "float",
            id: 6,
            new_value: 0,
            old_value: 1,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:1.000.00",
        "should display the correct content of tracked field of type float: from non-0 to 0 (Total: 1.00 -> 0.00)"
    );
});

QUnit.test('rendering of tracked field of type float: from 0 to non-0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "float",
            id: 6,
            new_value: 1,
            old_value: 0,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:0.001.00",
        "should display the correct content of tracked field of type float: from 0 to non-0 (Total: 0.00 -> 1.00)"
    );
});

QUnit.test('rendering of tracked field of type monetary: from non-0 to 0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "monetary",
            id: 6,
            new_value: 0,
            old_value: 1,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:1.000.00",
        "should display the correct content of tracked field of type monetary: from non-0 to 0 (Total: 1.00 -> 0.00)"
    );
});

QUnit.test('rendering of tracked field of type monetary: from 0 to non-0', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Total",
            field_type: "monetary",
            id: 6,
            new_value: 1,
            old_value: 0,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Total:0.001.00",
        "should display the correct content of tracked field of type monetary: from 0 to non-0 (Total: 0.00 -> 1.00)"
    );
});

QUnit.test('rendering of tracked field of type boolean: from true to false', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Is Ready",
            field_type: "boolean",
            id: 6,
            new_value: false,
            old_value: true,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Is Ready:TrueFalse",
        "should display the correct content of tracked field of type boolean: from true to false (Is Ready: True -> False)"
    );
});

QUnit.test('rendering of tracked field of type boolean: from false to true', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Is Ready",
            field_type: "boolean",
            id: 6,
            new_value: true,
            old_value: false,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Is Ready:FalseTrue",
        "should display the correct content of tracked field of type boolean: from false to true (Is Ready: False -> True)"
    );
});

QUnit.test('rendering of tracked field of type char: from a string to empty string', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Name",
            field_type: "char",
            id: 6,
            new_value: "",
            old_value: "Marc",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Name:Marc",
        "should display the correct content of tracked field of type char: from a string to empty string (Name: Marc ->)"
    );
});

QUnit.test('rendering of tracked field of type char: from empty string to a string', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Name",
            field_type: "char",
            id: 6,
            new_value: "Marc",
            old_value: "",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Name:Marc",
        "should display the correct content of tracked field of type char: from empty string to a string (Name: -> Marc)"
    );
});

QUnit.test('rendering of tracked field of type date: from no date to a set date', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Deadline",
            field_type: "date",
            id: 6,
            new_value: "2018-12-14",
            old_value: false,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Deadline:12/14/2018",
        "should display the correct content of tracked field of type date: from no date to a set date (Deadline: -> 12/14/2018)"
    );
});

QUnit.test('rendering of tracked field of type date: from a set date to no date', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Deadline",
            field_type: "date",
            id: 6,
            new_value: false,
            old_value: "2018-12-14",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Deadline:12/14/2018",
        "should display the correct content of tracked field of type date: from a set date to no date (Deadline: 12/14/2018 ->)"
    );
});

QUnit.test('rendering of tracked field of type datetime: from no date and time to a set date and time', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Deadline",
            field_type: "datetime",
            id: 6,
            new_value: "2018-12-14 13:42:28",
            old_value: false,
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Deadline:12/14/2018 13:42:28",
        "should display the correct content of tracked field of type datetime: from no date and time to a set date and time (Deadline: -> 12/14/2018 13:42:28)"
    );
});

QUnit.test('rendering of tracked field of type datetime: from a set date and time to no date and time', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Deadline",
            field_type: "datetime",
            id: 6,
            new_value: false,
            old_value: "2018-12-14 13:42:28",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Deadline:12/14/2018 13:42:28",
        "should display the correct content of tracked field of type datetime: from a set date and time to no date and time (Deadline: 12/14/2018 13:42:28 ->)"
    );
});

QUnit.test('rendering of tracked field of type text: from some text to empty', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Name",
            field_type: "text",
            id: 6,
            new_value: "",
            old_value: "Marc",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Name:Marc",
        "should display the correct content of tracked field of type text: from some text to empty (Name: Marc ->)"
    );
});

QUnit.test('rendering of tracked field of type text: from empty to some text', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Name",
            field_type: "text",
            id: 6,
            new_value: "Marc",
            old_value: "",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Name:Marc",
        "should display the correct content of tracked field of type text: from empty to some text (Name: -> Marc)"
    );
});

QUnit.test('rendering of tracked field of type selection: from a selection to no selection', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "State",
            field_type: "selection",
            id: 6,
            new_value: "",
            old_value: "ok",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "State:ok",
        "should display the correct content of tracked field of type selection: from a selection to no selection (State: ok ->)"
    );
});

QUnit.test('rendering of tracked field of type selection: from no selection to a selection', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "State",
            field_type: "selection",
            id: 6,
            new_value: "ok",
            old_value: "",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "State:ok",
        "should display the correct content of tracked field of type selection: from no selection to a selection (State: -> ok)"
    );
});

QUnit.test('rendering of tracked field of type many2one: from having a related record to no related record', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Author",
            field_type: "many2one",
            id: 6,
            new_value: "",
            old_value: "Marc",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Author:Marc",
        "should display the correct content of tracked field of type many2one: from having a related record to no related record (Author: Marc ->)"
    );
});

QUnit.test('rendering of tracked field of type many2one: from no related record to having a related record', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Author",
            field_type: "many2one",
            id: 6,
            new_value: "Marc",
            old_value: "",
        }],
    });
    await createMessageComponent(message);
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValue').textContent,
        "Author:Marc",
        "should display the correct content of tracked field of type many2one: from no related record to having a related record (Author: -> Marc)"
    );
});

QUnit.test('basic rendering of tracking value (monetary type)', async function (assert) {
    assert.expect(8);

    const { createMessageComponent } = await this.start({
        env: {
            session: {
                currencies: { 1: { symbol: '$', position: 'before' } },
            },
        },
    });
    const message = this.messaging.models['mail.message'].create({
        id: 11,
        tracking_value_ids: [{
            changed_field: "Revenue",
            currency_id: 1,
            field_type: "monetary",
            id: 6,
            new_value: 500,
            old_value: 1000,
        }],
    });

    await createMessageComponent(message);
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValue',
        "should display a tracking value"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueFieldName',
        "should display the name of the tracked field"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueFieldName').textContent,
        "Revenue:",
        "should display the correct tracked field name (Revenue)",
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueOldValue',
        "should display the old value"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueOldValue').innerHTML,
        "$ 1000.00",
        "should display the correct old value with the currency symbol ($ 1000.00)",
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueSeparator',
        "should display the separator"
    );
    assert.containsOnce(
        document.body,
        '.o_Message_trackingValueNewValue',
        "should display the new value"
    );
    assert.strictEqual(
        document.querySelector('.o_Message_trackingValueNewValue').innerHTML,
        "$ 500.00",
        "should display the correct new value with the currency symbol ($ 500.00)",
    );
});

QUnit.test('message should not be considered as "clicked" after clicking on its author name', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        author: [['insert', { id: 7, display_name: "Demo User" }]],
        body: "<p>Test</p>",
        id: 100,
    });
    await createMessageComponent(message);
    document.querySelector(`.o_Message_authorName`).click();
    await nextAnimationFrame();
    assert.doesNotHaveClass(
        document.querySelector(`.o_Message`),
        'o-clicked',
        "message should not be considered as 'clicked' after clicking on its author name"
    );
});

QUnit.test('message should not be considered as "clicked" after clicking on its author avatar', async function (assert) {
    assert.expect(1);

    const { createMessageComponent } = await this.start();
    const message = this.messaging.models['mail.message'].create({
        author: [['insert', { id: 7, display_name: "Demo User" }]],
        body: "<p>Test</p>",
        id: 100,
    });
    await createMessageComponent(message);
    document.querySelector(`.o_Message_authorAvatar`).click();
    await nextAnimationFrame();
    assert.doesNotHaveClass(
        document.querySelector(`.o_Message`),
        'o-clicked',
        "message should not be considered as 'clicked' after clicking on its author avatar"
    );
});

QUnit.test('message should not be considered as "clicked" after clicking on notification failure icon', async function (assert) {
    assert.expect(1);

    this.data['mail.channel'].records.push({ id: 10 });
    this.data['mail.message'].records.push({
        body: 'not empty',
        id: 10,
        model: 'mail.channel',
        res_id: 11,
    });
    this.data['mail.notification'].records.push({
        id: 11,
        mail_message_id: 10,
        notification_status: 'exception',
        notification_type: 'email',
    });
    const { createThreadViewComponent } = await this.start();
    const threadViewer = this.messaging.models['mail.thread_viewer'].create({
        hasThreadView: true,
        qunitTest: insertAndReplace(),
        thread: insert({
            id: 11,
            model: 'mail.channel',
        }),
    });
    await createThreadViewComponent(threadViewer.threadView);
    document.querySelector('.o_Message_notificationIconClickable.o-error').click();
    await nextAnimationFrame();
    assert.doesNotHaveClass(
        document.querySelector(`.o_Message`),
        'o-clicked',
        "message should not be considered as 'clicked' after clicking on notification failure icon"
    );
});

});
});
});
